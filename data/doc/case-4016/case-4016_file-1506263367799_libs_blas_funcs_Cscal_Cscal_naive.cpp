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

#include "functions/Cscal.hpp"

static const char* module_name = "Cscal_naive";
static const char* kernel_name = "Cscal_naive";

namespace iclgpu { namespace functions { namespace implementations {

bool Cscal_naive::accept(const Cscal::params& params, Cscal::score& score)
{
    return true;
}

event Cscal_naive::execute(const Cscal::params& params, const std::vector<event>& dep_events)
{
    auto engine = context()->get_engine();
    auto kernel = engine->get_kernel(kernel_name, module_name);

    size_t buf_size = params.n * params.incx;

    kernel->set_arg(0, params.alpha);
    auto buf_x = engine->get_inout_buffer(params.x, buf_size);
    kernel->set_arg(1, buf_x);
    kernel->set_arg(2, params.incx);

    auto gws = nd_range(params.n);
    auto lws = null_range;

    kernel->set_options({ gws, lws });
    return kernel->submit(dep_events);
}

} } } // namespace iclgpu::functions::implementations