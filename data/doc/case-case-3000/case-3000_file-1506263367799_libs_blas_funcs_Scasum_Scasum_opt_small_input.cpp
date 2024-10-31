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

#include "functions/Scasum.hpp"

static const char* module_name = "Scasum_opt_small_input";
static const char* kernel_name = "Scasum_opt_small_input";

namespace iclgpu { namespace functions { namespace implementations {

bool Scasum_opt_small_input::accept(const Scasum::params& params, Scasum::score& score)
{
    if (params.n <= 16)
    {
        score.n = 1.2f;
        return true;
    }
    else
    {
        return false;
    }
}

event Scasum_opt_small_input::execute(const Scasum::params& params, const std::vector<event>& dep_events)
{
    auto engine = context()->get_engine();
    auto kernel = engine->get_kernel(kernel_name, module_name);
    size_t buf_size = params.n * params.incx;

    kernel->set_arg(0, params.n);

    auto buf_x = engine->get_input_buffer(params.x, buf_size);
    kernel->set_arg(1, buf_x);

    kernel->set_arg(2, params.incx);

    auto buf_result = engine->get_inout_buffer(params.result, 1);
    kernel->set_arg(3, buf_result);

    nd_range gws = nd_range(16);
    nd_range lws = nd_range(16);

    auto options = kernel_options(gws, lws);
    kernel->set_options(options);

    return kernel->submit(dep_events);
}

} } }