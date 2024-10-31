#define __CL_ENABLE_EXCEPTIONS
#include <CL/cl.hpp>

#include <iostream>

int main () {
    try {
        std::vector<cl::Platform> platforms;
        cl::Platform::get (&platforms);
        if (platforms.size () == 0) {
            std::cout << "No OpenCL platforms detected" << std::endl;
            return -1;
        }

        unsigned int platformID (0);

        for (auto p : platforms) {
            std::string platformVendor, platformName;
            p.getInfo (CL_PLATFORM_VENDOR, &platformVendor);
            p.getInfo (CL_PLATFORM_NAME, &platformName);

            cl_context_properties properties[] = {
                CL_CONTEXT_PLATFORM,
                (cl_context_properties)(platforms[platformID])(),
                0
            };

            platformID++;

            try {
                cl::Context context (CL_DEVICE_TYPE_ALL, properties);
                std::vector<cl::Device> devices =
                    context.getInfo<CL_CONTEXT_DEVICES> ();
            } catch (cl::Error err) {
                continue;
            }

            std::cout << platformVendor << " (" << platformName << ")"
                      << std::endl;
        }
    } catch (cl::Error err) {
        std::cerr << "ERROR: " << err.what () << "(" << err.err () << ")"
                  << std::endl;
    }

    return 0;
}