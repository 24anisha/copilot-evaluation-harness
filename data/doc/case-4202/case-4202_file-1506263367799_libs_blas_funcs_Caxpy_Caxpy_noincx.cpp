// Copyright (c) 2017-2018 Intel Corporation
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//      http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "functions/Caxpy.hpp"

static const char* module_name = "Caxpy_noincx";
static const char* kernel_name = "Caxpy_noincx";

namespace iclgpu { namespace functions { namespace implementations {

bool Caxpy_noincx::accept(const Caxpy::params& params, Caxpy::score& score)
{
    if (params.incx != 1) return false;
    score.incx = 1.1f;
    return true;
}

Caxpy_noincx::command_builder Caxpy_noincx::selected()
{
    auto engine = context()->get_engine();
    auto kernel = engine->get_kernel(kernel_name, module_name);
    return [=](const Caxpy::params& params)
    {
        size_t x_buf_size = params.n;
        size_t y_buf_size = params.n * params.incy;

        kernel->set_arg(0, params.alpha);
        auto buf_x = engine->get_input_buffer(params.x, x_buf_size);
        kernel->set_arg(1, buf_x);
        auto buf_y = engine->get_inout_buffer(params.y, y_buf_size);
        kernel->set_arg(2, buf_y);
        kernel->set_arg(3, params.incy);

        auto gws = nd_range(params.n);
        auto lws = null_range;
        kernel->set_options({ gws, lws });
        return kernel;
    };
}

} } } // namespace iclgpu::functions::implementations