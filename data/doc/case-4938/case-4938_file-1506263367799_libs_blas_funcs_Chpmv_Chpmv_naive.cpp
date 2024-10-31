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

#include "functions/Chpmv.hpp"

static const char* module_name = "Chpmv_naive";
static const char* kernel_name = "Chpmv_naive";

namespace iclgpu { namespace functions { namespace implementations {

bool Chpmv_naive::accept(const Chpmv::params& params, Chpmv::score& score)
{
    return true;
}

event Chpmv_naive::execute(const Chpmv::params& params, const std::vector<event>& dep_events)
{
    auto engine = context()->get_engine();
    auto kernel = engine->get_kernel(kernel_name, module_name);
    size_t a_buf_size = params.n * (params.n + 1)/2;
    size_t x_buf_size = params.n * params.incx;
    size_t y_buf_size = params.n * params.incy;

    kernel->set_arg(0, params.uplo);
    kernel->set_arg(1, params.n);
    kernel->set_arg(2, params.alpha);
    auto buf_a = engine->get_input_buffer(params.AP, a_buf_size);
    kernel->set_arg(3, buf_a);
    auto buf_x = engine->get_input_buffer(params.x, x_buf_size);
    kernel->set_arg(4, buf_x);
    kernel->set_arg(5, params.incx);
    kernel->set_arg(6, params.beta);
    auto buf_y = engine->get_inout_buffer(params.y, y_buf_size);
    kernel->set_arg(7, buf_y);
    kernel->set_arg(8, params.incy);

    auto gws = nd_range(params.n);
    auto lws = null_range;
    kernel->set_options({ gws, lws });

    return kernel->submit(dep_events);
}

} } } // namespace iclgpu::functions::implementations