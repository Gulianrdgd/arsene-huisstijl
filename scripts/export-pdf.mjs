// Headless-Chromium PDF export for the Arsene brand book.
//
// Renders the app with a real browser engine and writes a vector PDF.
// Unlike Firefox's "Save to PDF", this forces backgrounds on and uses the CSS
// @page size (no fit-to-page scaling), so the output matches the screen.
//
// Usage:
//   npm run export:pdf            # auto-starts a dev server, writes arsene-huisstijl.pdf
//   npm run export:pdf -- --verify  # also dumps screen-vs-print screenshots to .export-check/
//
// If a server is already running on URL it is reused; otherwise one is started
// and stopped automatically.
//   URL=http://localhost:5173 OUT=book.pdf npm run export:pdf

import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';

const TARGET = process.env.URL ?? 'http://localhost:5173/';
const OUT = process.env.OUT ?? 'arsene-huisstijl.pdf';
const VERIFY = process.argv.includes('--verify');

async function reachable(url) {
  try {
    const res = await fetch(url, { signal: AbortSignal.timeout(1500) });
    return res.ok;
  } catch {
    return false;
  }
}

async function waitFor(url, timeoutMs = 30000) {
  const end = Date.now() + timeoutMs;
  while (Date.now() < end) {
    if (await reachable(url)) return true;
    await new Promise((r) => setTimeout(r, 400));
  }
  return false;
}

let server;
if (!(await reachable(TARGET))) {
  const port = new URL(TARGET).port || '5173';
  console.log(`Starting dev server on port ${port}…`);
  server = spawn('npm', ['run', 'dev', '--', '--port', port], { stdio: 'ignore' });
  if (!(await waitFor(TARGET))) {
    server.kill();
    throw new Error(`Dev server did not come up at ${TARGET}`);
  }
}

const browser = await chromium.launch();
try {
  const page = await browser.newPage();
  await page.goto(TARGET, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  const pageCount = await page.locator('.page').count();
  console.log(`Found ${pageCount} pages at ${TARGET}`);

  // page.pdf always renders print media; force it explicitly to be safe.
  await page.emulateMedia({ media: 'print' });
  await page.pdf({
    path: OUT,
    printBackground: true,   // keep background colors / gradients
    preferCSSPageSize: true, // honour @page { size: A4; margin: 0 } — no scaling
  });
  console.log(`Wrote ${OUT}`);
} finally {
  await browser.close();
  if (server) server.kill();
}

// --verify rasterizes the *actual* PDF (not the page) to images, so effects
// that only break in the vector PDF — blurred shadows, gradients — are visible.
if (VERIFY) {
  const { pdf } = await import('pdf-to-img');
  await mkdir('.export-check', { recursive: true });
  const doc = await pdf(OUT, { scale: 2 });
  let i = 0;
  for await (const png of doc) {
    i++;
    await writeFile(`.export-check/pdf-page-${i}.png`, png);
  }
  console.log(`Rendered ${i} PDF pages to .export-check/`);
}
