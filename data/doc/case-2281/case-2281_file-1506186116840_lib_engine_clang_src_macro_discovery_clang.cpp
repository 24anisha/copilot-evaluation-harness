// Metashell - Interactive C++ template metaprogramming shell
// Copyright (C) 2016, Abel Sinkovics (abel@sinkovics.hu)
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#include <metashell/engine/clang/macro_discovery.hpp>

namespace metashell
{
  namespace engine
  {
    namespace clang
    {
      macro_discovery::macro_discovery(binary binary_) : _binary(binary_) {}

      data::cpp_code macro_discovery::macros(const iface::environment& env_)
      {
        const data::process_output output =
            run_clang(_binary, {"-dM", "-E"}, env_.get_all());

        if (exit_success(output))
        {
          return data::cpp_code(output.standard_output);
        }
        else
        {
          throw std::runtime_error("Error getting list of macros: " +
                                   output.standard_error);
        }
      }
    } // namespace clang
  } // namespace engine
} // namespace metashell