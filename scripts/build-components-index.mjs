// Generates design-system/index.html: every component preview on one page.
// Each components/<Name>/preview.html starts with <!-- @dsCard group="..." height=... -->.
//   node scripts/build-components-index.mjs
import { readdir, readFile, writeFile } from 'node:fs/promises';

const root = new URL('../design-system/', import.meta.url);
const order = ['Merk', 'Detail', 'Tekst', 'Data', 'Web', 'Print', 'Toepassingen'];
const groups = new Map(order.map((g) => [g, []]));

for (const entry of await readdir(new URL('components/', root), { withFileTypes: true })) {
	if (!entry.isDirectory()) continue;
	const html = await readFile(new URL(`components/${entry.name}/preview.html`, root), 'utf8');
	const m = html.match(/@dsCard group="([^"]+)" height=(\d+)/);
	if (!m) throw new Error(`${entry.name}: missing @dsCard comment`);
	if (!groups.has(m[1])) groups.set(m[1], []);
	groups.get(m[1]).push({ name: entry.name, height: Number(m[2]) });
}

const sections = [...groups]
	.filter(([, items]) => items.length)
	.map(([group, items]) => {
		const cards = items
			.sort((a, b) => a.name.localeCompare(b.name))
			.map(({ name, height }) =>
				`<section><h3><a href="components/${name}/README.md">${name}</a></h3><iframe src="components/${name}/preview.html" style="height:${height + 48}px" loading="lazy" title="${name}"></iframe></section>`)
			.join('\n');
		return `<h2>${group}</h2>\n${cards}`;
	})
	.join('\n');

const page = `<!doctype html>
<html lang="nl">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Arsene componenten</title>
<link rel="icon" href="../assets/logo/arsene-icon.svg">
<link rel="stylesheet" href="tokens.css">
<style>
body{margin:0;padding:48px 24px 96px;font-family:var(--font-sans);color:var(--ink);background:var(--paper)}
main{max-width:1100px;margin:0 auto}
h1{font-size:44px;line-height:1.05;letter-spacing:-.035em;margin:0 0 16px}
h2{font-size:14px;font-weight:600;margin:56px 0 12px;padding-top:12px;border-top:1px solid var(--ink)}
h3{font-size:14px;font-weight:600;margin:0 0 8px} h3 a{color:var(--ink);text-decoration:underline 1px var(--mint-deep);text-underline-offset:.2em}
section{margin:0 0 24px} iframe{width:100%;border:0;border-radius:var(--radius-surface);background:var(--paper);box-shadow:0 0 0 1px var(--warm-400)}
p{max-width:65ch;color:var(--warm-800);line-height:1.55;margin:0}
code{font-family:var(--font-mono);font-size:.9em}
</style></head>
<body><main>
<h1>Arsene componenten.</h1>
<p>Alle voorbeelden uit <code>components/</code>, gegenereerd door <code>scripts/build-components-index.mjs</code>. De regels staan per component in de README (klik op de naam). Open via een lokale server in de repo-root, bijvoorbeeld <code>python3 -m http.server</code>, zodat fonts en logo's laden.</p>
${sections}
</main></body></html>
`;

await writeFile(new URL('index.html', root), page);
console.log('wrote design-system/index.html');
