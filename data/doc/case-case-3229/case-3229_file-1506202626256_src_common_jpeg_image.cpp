// This file is distributed under the MIT license.
// See the LICENSE file for details.

#include <common/config.h>

#include <csetjmp>
#include <cstdio>

#if VSNRAY_COMMON_HAVE_JPEG
#include <jpeglib.h>
#endif

#include "cfile.h"
#include "jpeg_image.h"

namespace visionaray
{

#if VSNRAY_COMMON_HAVE_JPEG
struct error_mngr
{
    jpeg_error_mgr pub;
    jmp_buf jmpbuf;
};

static void error_exit_func(j_common_ptr info)
{
    error_mngr* err = reinterpret_cast<error_mngr*>(info->err);
    // TODO: print debug info
    longjmp(err->jmpbuf, 1);
}

struct decompress_ptr
{
    jpeg_decompress_struct* info;

    decompress_ptr() : info(0) {}

   ~decompress_ptr()
    {
        jpeg_finish_decompress(info);
        jpeg_destroy_decompress(info);
    }
};
#endif


bool jpeg_image::load(std::string const& filename)
{
#if VSNRAY_COMMON_HAVE_JPEG
    cfile file(filename.c_str(), "r");

    if (!file.good())
    {
        return false;
    }

    struct jpeg_decompress_struct info;
    decompress_ptr info_ptr;
    error_mngr err;

    info.err = jpeg_std_error(&err.pub);
    err.pub.error_exit = error_exit_func;

    if (setjmp(err.jmpbuf))
    {
        return false; // TODO?
    }

    jpeg_create_decompress(&info);

    info_ptr.info = &info;

    jpeg_stdio_src(&info, file.get());

    jpeg_read_header(&info, TRUE);
    width_      = info.image_width;
    height_     = info.image_height;
    auto pitch  = width_ * 3;

    jpeg_start_decompress(&info);

    data_.resize(pitch * height_);

    while (info.output_scanline < info.output_height)
    {
        unsigned char* row = data_.data() + (info.output_height - 1 - info.output_scanline) * pitch;

        jpeg_read_scanlines(&info, &row, 1);
    }

    return true;
#else
    VSNRAY_UNUSED(filename);

    return false;
#endif
}

} // visionaray