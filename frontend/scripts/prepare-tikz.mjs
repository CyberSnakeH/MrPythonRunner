// Ship the pinned TikZJax worker, TeX runtime and fonts with the offline app.
import { cp, mkdir, readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
const root = new URL('../', import.meta.url);
const source = new URL('node_modules/@rod2ik/tikzjax/', root);
const target = new URL('public/vendor/tikzjax/', root);
await mkdir(target, { recursive: true });
await cp(fileURLToPath(new URL('dist/', source)), fileURLToPath(target), { recursive: true });
await cp(fileURLToPath(new URL('LICENSE', source)), fileURLToPath(new URL('LICENSE', target)));
const { version } = JSON.parse(await readFile(new URL('package.json', source), 'utf8'));
await writeFile(new URL('VERSION.txt', target), `@rod2ik/tikzjax ${version}\nhttps://github.com/rod2ik/tikzjax\n`);
