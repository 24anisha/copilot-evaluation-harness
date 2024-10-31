/*
 * Copyright 2015 WebAssembly Community Group
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


#include "BreakpointEnvironment.h"

#include "Breakpoint.h"
#include <interpreter/VMState.h>

namespace wasmint {
    std::string BreakpointEnvironment::returnValue() {
        if (breakpoint_->instruction()->returnType() == wasm_module::Void::instance()) {
            return "";
        } else {
            // FIXME: dummy code
            return "dummy";
        }
    }
}