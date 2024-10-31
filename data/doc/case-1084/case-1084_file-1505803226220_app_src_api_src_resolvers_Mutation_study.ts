import { getUserId, Context } from '../../utils'
import { uniqueId } from 'lodash';

export const study = {
  async createStudy(parent, { owner, imageURL, description }, ctx: Context, info) {
    owner = owner ? { connect: { email: owner }, } : {};
    return ctx.db.mutation.createStudy(
      {
        data: {
          imageURL,
          shortCode: uniqueId(),
          description,
          owner
        },
      },
      info
    )
  },
};