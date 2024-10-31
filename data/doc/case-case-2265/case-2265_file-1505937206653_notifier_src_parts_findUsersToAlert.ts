import {
  SEND_EMAIL_AND_UPDATE_ALERTED,
  ONLY_UPDATE_ALERTED,
} from "./constants";
import { FullUser, ActionableUser, User } from "./interfaces";

export default function findUsersToAlert(users: FullUser[]): ActionableUser[] {
  return users
    .map(withActionableRepos)
    .filter(
      ({ actionableRepos: repos }) =>
        repos[SEND_EMAIL_AND_UPDATE_ALERTED].length ||
        repos[ONLY_UPDATE_ALERTED].length
    );
}

function withActionableRepos(user: FullUser) {
  const { repos, alerted } = user;
  const base = {
    [SEND_EMAIL_AND_UPDATE_ALERTED]: [],
    [ONLY_UPDATE_ALERTED]: [],
  };
  const actionableRepos = repos.reduce((result, { repo, tags }) => {
    tags = tags.length ? tags : [{ name: "", entry: "" }];
    if (tags[0].name === alerted[repo]) {
      return result;
    }
    pushRepoWithNewTags(result, tags, alerted, repo);
    return result;
  }, base);
  return { ...user, actionableRepos };
}

function pushRepoWithNewTags(result, tags, alerted, repo) {
  if (!alerted[repo] || !tags[0].name) {
    result[ONLY_UPDATE_ALERTED].push({ repo, tags: [tags[0]] });
    return;
  }
  const alertedIndex = tags.map((t) => t.name).indexOf(alerted[repo]);
  const newTags = alertedIndex > -1 ? tags.slice(0, alertedIndex) : [tags[0]];
  result[SEND_EMAIL_AND_UPDATE_ALERTED].push({ repo, tags: newTags });
}