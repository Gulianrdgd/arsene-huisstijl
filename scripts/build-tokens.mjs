// Generates design-system/tokens.css from design-system/tokens.json.
//   node scripts/build-tokens.mjs
import { readFile, writeFile } from 'node:fs/promises';

const dir = new URL('../design-system/', import.meta.url);
const t = JSON.parse(await readFile(new URL('tokens.json', dir), 'utf8'));

const palette = new Set(t.color.palette.map((c) => c.name));
const ref = (v) => (palette.has(v) ? `var(--${v})` : v);
const note = (s) => ` /* ${s.replace(/\*\//g, '* /')} */`;
const block = (selector, lines) => `${selector} {\n${lines.map((l) => `  ${l}`).join('\n')}\n}`;

const out = ['/* Arsene: generated from tokens.json by scripts/build-tokens.mjs. Do not edit by hand. */'];

// Fonts (latin + latin-ext, variable weight)
const ranges = {
	latin: 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD',
	'latin-ext': 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'
};
for (const f of t.font) {
	for (const file of f.files) {
		const subset = file.includes('latin-ext') ? 'latin-ext' : 'latin';
		out.push(block('@font-face', [
			`font-family: "${f.family}";`,
			'font-style: normal;',
			'font-display: swap;',
			`font-weight: ${f.weights};`,
			`src: url("./fonts/${file}") format("woff2-variations");`,
			`unicode-range: ${ranges[subset]};`
		]));
	}
}

// Palette, fonts and sizes
out.push(block(':root', [
	...t.color.palette.map((c) => `--${c.name}: ${c.value};${note(c.usage)}`),
	...t.font.map((f) => `--${f.name}: ${f.stack};${note(f.usage)}`),
	...t.size.map((s) => `--${s.name}: ${s.value};${note(s.usage)}`)
]));

// Web roles: light by default, dark via data-theme or the system preference
const roles = [...t.color.roles.tokens, ...t.color.chart.tokens];
const light = roles.map((r) => `--${r.name}: ${ref(r.light)};${note(r.usage)}`);
const dark = roles.map((r) => `--${r.name}: ${ref(r.dark)};`);
out.push(block(':root, [data-theme="light"]', light));
out.push(block('[data-theme="dark"]', dark));
out.push(`@media (prefers-color-scheme: dark) {\n${block(':root:not([data-theme="light"])', dark).replace(/^/gm, '  ')}\n}`);

// Type styles
for (const [medium, styles] of Object.entries(t.type)) {
	out.push(`/* Type: ${medium} */`);
	for (const s of styles) {
		const lines = [
			`font-family: var(--${s.font ?? 'font-sans'});`,
			`font-size: ${s.size};`,
			`line-height: ${s.line};`,
			`font-weight: ${s.weight};`,
			`letter-spacing: ${s.tracking};`
		];
		if (s.case) lines.push(`text-transform: ${s.case};`);
		out.push(`/* ${s.usage} */\n${block(`.${s.name}`, lines)}`);
	}
}

await writeFile(new URL('tokens.css', dir), out.join('\n\n') + '\n');
console.log('wrote design-system/tokens.css');
