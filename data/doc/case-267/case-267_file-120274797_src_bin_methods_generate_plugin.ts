import * as fs from "fs";
import * as path from "path";
import { PackageJson } from "type-fest";
import { CLI, utils, ParamsFrom } from "./../../../index";

const PackageJSON: PackageJson = JSON.parse(
  fs
    .readFileSync(path.join(__dirname, "..", "..", "..", "..", "package.json"))
    .toString()
);

export class GeneratePluginCLI extends CLI {
  name = "generate-plugin";
  description =
    "Generate the structure of a new actionhero plugin in an empty directory";
  example = "actionhero generate plugin";

  async run() {
    let templateBuffer = fs.readFileSync(
      path.join(
        __dirname,
        "/../../../../templates/package-plugin.json.template"
      )
    );
    let template = String(templateBuffer);

    const regex = new RegExp("%%versionNumber%%", "g");
    template = template.replace(regex, PackageJSON.version);

    [
      "actions",
      "tasks",
      "initializers",
      "servers",
      "config",
      "bin",
      "public",
    ].forEach((type) => {
      try {
        const message = utils.fileUtils.createDirSafely(
          path.join(process.cwd(), type)
        );
        console.info(message);
      } catch (error) {
        console.log(error.toString());
      }
    });

    const message = utils.fileUtils.createFileSafely(
      path.join(process.cwd(), "package.json"),
      template
    );
    console.info(message);

    return true;
  }
}