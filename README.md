# Arsene Huisstijl

The Arsene brand book — a SvelteKit app that renders the house-style guide as an
11-page A4 document, plus a one-command export to a print-ready PDF.

📄 **[Download the PDF →](./arsene-huisstijl.pdf)**

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
