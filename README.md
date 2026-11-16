# Arsene huisstijl

Alles om iets in de Arsene-huisstijl te maken: de regels, de tokens, de componenten, de logo's en de fonts, plus het brand book als A4-document.

Download het brand book: [arsene-huisstijl.pdf](./arsene-huisstijl.pdf).

## Wat staat waar

| Map | Inhoud |
| --- | --- |
| [`design-system/`](design-system/) | De regels: [`README.md`](design-system/README.md) (kleur, typografie, logo, detailtaal, vorm), [`schrijven.md`](design-system/schrijven.md) (toon, opmaak, taglines), [`web.md`](design-system/web.md) (sites en apps, licht en donker), [`print.md`](design-system/print.md) (A4-documenten). Tokens in [`tokens.json`](design-system/tokens.json) (bron) en `tokens.css` (gegenereerd), webfonts in `fonts/`, componenten met regels en voorbeeld in [`components/`](design-system/components/), alle voorbeelden op één pagina in `index.html`. |
| [`assets/logo/`](assets/logo/) | Woordmerk en beeldmerk als SVG (ink voor licht, paper voor donker), het app-icoon, en de Illustrator-bron in `bron/`. |
| [`assets/icons/`](assets/icons/) | Een selectie Phosphor-iconen (Regular, MIT). |
| [`templates/`](templates/) | Word- en PowerPoint-sjablonen: document, brief, presentatie. |
| [`fonts/`](fonts/) | Geist en Geist Mono als desktopfonts voor Office (OFL). De webfonts staan in `design-system/fonts/`. |
| [`src/`](src/) | Het brand book: een SvelteKit-app die de huisstijl als A4-document toont en dezelfde tokens gebruikt. |
| [`scripts/`](scripts/) | `build-tokens.mjs`, `build-icons-preview.mjs` en `build-components-index.mjs` (`yarn tokens`), `build-logos.py`, `build-office.py`, `export-pdf.mjs` (`yarn export:pdf`). |

## Gebruiken met Claude Code

Geef Claude Code deze repo (of kopieer hem naast je project) en vraag het iets te bouwen "in de Arsene-huisstijl". [`CLAUDE.md`](CLAUDE.md) vertelt het welke bestanden het moet lezen en welke regels het vaakst misgaan.

## Snel aan de slag op het web

```html
<link rel="stylesheet" href="design-system/tokens.css">
<link rel="stylesheet" href="design-system/components/bundle.css">
<body class="ar">
  <h1 class="web-heading-1">Software op <span class="ar-marker">jouw</span> voorwaarden.</h1>
  <a class="ar-button" href="/contact">Begin een gesprek →</a>
</body>
```

Zie [`design-system/web.md`](design-system/web.md) voor Tailwind en de donkere modus.

## Licenties

Geist en Geist Mono vallen onder de SIL Open Font License (`design-system/licenses/`, `fonts/OFL.txt`). De iconen zijn van Phosphor Icons (MIT, `assets/icons/LICENSE-phosphor.txt`). Logo's en beeld zijn van Arsene, alleen voor Arsene-materiaal.

---

The rest of this README covers the brand book app.

## Developing

Install dependencies with `yarn`, then start a dev server:

```sh
yarn dev

# or open it in a new browser tab
yarn dev -- --open
```

## Exporting the PDF

```sh
yarn export:pdf
```

This renders the pages with a headless Chromium engine and writes
`arsene-huisstijl.pdf` (vector, selectable text, ~700 KB). It auto-starts a dev
server if one isn't already running, and shuts it down afterwards.

Add `--verify` to also rasterize the generated PDF into `.export-check/` so you
can eyeball every page:

```sh
yarn export:pdf --verify
```

Why a headless render instead of the browser's "Save as PDF": it uses the same
engine every time (no Chrome-vs-Firefox differences), forces backgrounds on, and
honours the CSS A4 page size, so the output matches the screen.

## Building

To create a production version of the app:

```sh
yarn build
```

Preview the production build with `yarn preview`.

> To deploy, you may need a SvelteKit [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
