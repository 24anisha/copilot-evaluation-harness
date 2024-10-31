import { doGenerate } from '../libs/generator';
import { default as PostModel, PostDocumentI, PostI } from '../models/post';
import * as _ from 'lodash';
import markdownGenerator from '../libs/generator/markdown';

export function createPost(post: PostI, cb?: (err: any, document: PostDocumentI, numAffected: number) => void) {
  if (!post.content) {
    post = generatePost(post, {});
  }
  return new PostModel(post)
    .save(cb);
}

export function generatePost(post: PostI, option: any) {
  post = _.cloneDeep(post);
  post.content = doGenerate(post.source, post.sourceType, option);
  return post;
}