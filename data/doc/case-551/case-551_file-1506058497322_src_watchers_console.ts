import * as fs from "fs";
import {Watcher} from "./watcher";
import {ID} from "../runtime/runtime";

export class ConsoleWatcher extends Watcher {

  setup() {
    if(console) {
      this.program
      .watch("Print to console log.", ({find, record}) => {
        let log = find("console/log");
        return [log.add("text", log.text)]
      })
      .asDiffs(({adds}) => {
        for(let [log, _, text] of adds) {
          console.log(text);
        }
      })
      .watch("Print to console error.", ({find, record}) => {
        let log = find("console/error");
        return [log.add("text", log.text)]
      })
      .asDiffs(({adds}) => {
        for(let [log, _, text] of adds) {
          console.error(text);
        }
      })
      .watch("Print to console warn.", ({find, record}) => {
        let log = find("console/warn");
        return [log.add("text", log.text)]
      })
      .asDiffs(({adds}) => {
        for(let [log, _, text] of adds) {
          console.warn(text);
        }
      })
    }
  }
}

Watcher.register("console", ConsoleWatcher);