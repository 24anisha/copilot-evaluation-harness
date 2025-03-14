#include <SWFTag.h>
#include "gSWF.h"
#include <cstdint>
#include <cstring>

namespace SWF {
	Tag *Tag::get(Reader *r, int end, Context *ctx) {
		std::uint16_t h = r->getWord();
		int type = h>>6;
		int len = h&0x3F;
		if (len == 0x3F) { // long size
			len = r->getInt();
		}

		// sanity check
		if (len > 100000000) {
			fprintf(stderr,"ridiculous tag size: %i, ignoring.\n", len);
			return NULL;
		}

		Tag *ret = getByType(type);

		if (!ret) {
			ret = new UnknownTag;
		}

		ret->setType(type);
		ret->setLength(len);
		ret->parse(r, r->getPosition()+len, ctx);

		return ret;
	}

	void Tag::writeHeader(Writer *w, Context *ctx, size_t len) {
		// FIXME shouldnt this be 0x3f - macromedia flash seems to use long length for > 1F...
		len -= (len >= SWF_LONG_TAG + 6) ? 6 : 2;
		std::uint16_t h = type<<6;
		if (len >= SWF_LONG_TAG) {
			h |= 0x3F;
			w->putWord(h);
			w->putInt(len);
		} else {
			h |= len;
			w->putWord(h);
		}
	}
}