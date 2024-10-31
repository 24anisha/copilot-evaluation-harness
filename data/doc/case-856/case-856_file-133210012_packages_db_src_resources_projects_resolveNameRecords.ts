import { logger } from "@truffle/db/logger";
const debug = logger("db:resources:projects:resolveNameRecords");

import type {
  SavedInput,
  IdObject,
  Workspace
} from "@truffle/db/resources/types";

export async function resolveNameRecords(
  project: IdObject<"projects">,
  inputs: {
    name?: string;
    type?: string;
  },
  context: {
    workspace: Workspace;
  },
  _?
): Promise<SavedInput<"nameRecords">[]> {
  const { id } = project;
  const { name, type } = inputs;
  const { workspace } = context;

  const projectNames = await workspace.find("projectNames", {
    selector: {
      "project.id": id,
      "key.name": name,
      "key.type": type
    }
  });

  const nameRecords = await workspace.find(
    "nameRecords",
    projectNames.map(
      projectName => projectName?.nameRecord as IdObject<"nameRecords">
    )
  );

  return nameRecords.filter(
    (nameRecord): nameRecord is SavedInput<"nameRecords"> => !!nameRecord
  );
}