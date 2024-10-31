/**
 * @category Internal processor
 * @packageDocumentation
 */
import { logger } from "@truffle/db/logger";
const debug = logger("db:project:loadCompile:bytecodes");

import type { IdObject, Input } from "@truffle/db/resources";
import { resources } from "@truffle/db/process";
import * as Batch from "./batch";

export const process = Batch.Contracts.configure<{
  compilation: {};
  contract: {
    bytecode: Input<"bytecodes">;
    deployedBytecode: Input<"bytecodes">;
  };
  source: {};
  resources: {
    callBytecode: IdObject<"bytecodes"> | undefined;
    createBytecode: IdObject<"bytecodes"> | undefined;
  };
  entry: {
    callBytecode: Input<"bytecodes">;
    createBytecode: Input<"bytecodes">;
  };
  result: {
    callBytecode: IdObject<"bytecodes"> | undefined;
    createBytecode: IdObject<"bytecodes"> | undefined;
  };
}>({
  extract({
    input: { bytecode: createBytecode, deployedBytecode: callBytecode }
  }) {
    return {
      createBytecode,
      callBytecode
    };
  },

  *process({ entries }) {
    const callBytecodes = yield* resources.load(
      "bytecodes",
      entries.map(({ callBytecode }) => callBytecode)
    );

    const createBytecodes = yield* resources.load(
      "bytecodes",
      entries.map(({ createBytecode }) => createBytecode)
    );

    return callBytecodes.map((callBytecode, index) => ({
      callBytecode,
      createBytecode: createBytecodes[index]
    }));
  },

  convert({ result: { callBytecode, createBytecode }, input: contract }) {
    return {
      ...contract,
      db: {
        ...contract.db,
        callBytecode,
        createBytecode
      }
    };
  }
});