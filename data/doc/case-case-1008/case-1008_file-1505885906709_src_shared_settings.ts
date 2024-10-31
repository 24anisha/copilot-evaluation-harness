
import * as os from 'os';
import * as path from 'path';
import * as fs from 'fs';

import * as helpers from './helpers';

// Global variables.

export const cachePath = path.join(os.homedir(), '.posthaste');
export const settingsPath = `${cachePath}/settings.json`;

var settings: any;

export function get(key: string) {
    ensureFile();

    return settings[key];
}

export function set(key: string, value: string) {
    ensureFile();

    settings[key] = value;
    fs.writeFileSync(settingsPath, JSON.stringify(settings, null, 2));
}

function ensureFile() {
    if(!settings) {
        if(!fs.existsSync(settingsPath)) {
            fs.writeFileSync(settingsPath, '{}');
        }

        settings = JSON.parse(fs.readFileSync(settingsPath).toString());
    }
}