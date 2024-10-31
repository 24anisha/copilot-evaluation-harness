/* eslint-disable @typescript-eslint/no-var-requires */
/* eslint-disable max-statements, complexity */
const AnsiConvert = require("ansi-to-html");
const convert = new AnsiConvert();

const BunyanLevelLookup = {
  60: "error",
  50: "error",
  40: "warn",
  30: "info",
  20: "debug",
  10: "silly"
};

const tagLevelMap = {
  "warn:": "warn",
  "error:": "error",
  fail: "error",
  rejection: "error",
  unhandled: "error",
  exception: "error",
  "debugger listening on": "silly"
};

/**
 * @param str
 * @param last
 */
export function parse(str: string, last: any) {
  let jsonData;
  let show;

  try {
    if (str[0] === "{" || str[0] === "[") {
      jsonData = JSON.parse(str);
    }
  } catch {
    //
  }

  let message;
  let level;

  if (jsonData) {
    level = BunyanLevelLookup[jsonData.level];
    message = str;
    if (level === "warn" || level === "error") {
      show = 2;
    }
  }

  if (!level) {
    const match = str.match(
      /warn\:|error\:|fail|rejection|unhandled|exception|debugger listening on/i
    );

    if (match) {
      const tag = match[0].toLowerCase();
      if (!level) {
        level = tagLevelMap[tag];
      }
      show = tag === "debugger listening on" ? 1 : 2;
    }
  }

  const entry: any = {
    level: level || "info",
    ts: Date.now(),
    message: message || str,
    json: jsonData,
    show
  };

  if (last && entry.ts === last.ts) {
    entry.tx = (last.tx || 0) + 1;
  }

  return entry;
}

/**
 * @param event
 */
export function getLogEventAsHtml(event) {
  return `${convert.toHtml(event.message)}`;
}