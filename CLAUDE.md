# Arsene design system

Gebruik deze repo als bron voor alles in de Arsene-huisstijl: websites, webapps, documenten, slides, e-mail.

## Voordat je iets maakt

- Lees eerst `design-system/README.md` en `design-system/schrijven.md`. Voor websites en apps ook `design-system/web.md`, voor A4-documenten `design-system/print.md`. Per bouwsteen staan regels en een voorbeeld in `design-system/components/<Naam>/`.
- Kleuren, fonts, tekststijlen en maten komen uit `design-system/tokens.json` (op het web `design-system/tokens.css`). Verzin geen waarden, ook geen tinten of extra grijzen. Op het web de rollen `web-*`, zodat licht en donker allebei werken.
- Kopieer voor een nieuw project `design-system/tokens.css`, `design-system/fonts/`, `design-system/components/bundle.css` en de logo's uit `assets/logo/`. Host de fonts zelf.

## Regels die het vaakst misgaan

- Geen eyebrow of kopregel: geen klein label in kapitalen boven een titel. Een sectie begint met de titel en een lede.
- Geen em dash (—), geen emoji, geen Title Case. Zinsvorm overal. Kapitalen alleen in Geist Mono voor korte metadata (paginanummer, lopende kop, tags).
- Logo altijd als bestand uit `assets/logo/` (ink op licht, paper op donker). Nooit "arsene" zelf zetten in Geist als logo, nooit kapitalen, de pin blijft mint.
- Mint is nooit tekst op paper. Op een mint vlak alleen `teal-deep` tekst, nooit wit.
- Nadruk met de marker op één of twee woorden, niet met vet. Vet is voor koppen.
- Weinig kaders: een dunne lijn in `ink` boven een blok, een vlak in `warm-200` alleen rond een demo. Geen schaduwen, geen gradients, geen pillen.
- Op het web nooit `warm-600` als tekstkleur (3,0:1); gebruik `web-text-muted`.
- Schrijf droog en concreet, jij en we, zonder consultancy-jargon (zie `schrijven.md`).

## Iconen, grafieken en Office

- Iconen alleen uit `assets/icons/` (Phosphor Regular), in de tekstkleur, 16 tot 24 px. Ontbreekt er een, haal hem uit Phosphor Regular; geen andere iconensets. Zie `components/Iconen`.
- Grafieken met de `chart-*` tokens volgens `components/Grafiek`: liefst één reeks uitgelicht, maximaal vier kleuren, legenda plus directe labels, tooltip en tabel op het web.
- Websites eindigen met de `Websitefooter`.
- Word en PowerPoint: begin vanuit `templates/` (zie `print.md`). Wil je de sjablonen aanpassen, doe dat in `scripts/build-office.py`.

## Wat nog niet vastligt

Fotografie en illustratie staan nog niet in het brand book. Verzin daar geen stijl voor; houd het sober en vraag het na. Onderdelen in `web.md` gemarkeerd met *voorstel* (o.a. de donkere modus) zijn afgeleid, nog niet vastgesteld.

## Deze repo aanpassen

- Tokens: wijzig `design-system/tokens.json` en draai `yarn tokens` (maakt `tokens.css`, het iconenoverzicht en `design-system/index.html`). Nooit `tokens.css` met de hand bewerken.
- Office-sjablonen: `python3 scripts/build-office.py` (vereist `python-docx`, `python-pptx` en `rsvg-convert`).
- Logo's: de bron is `assets/logo/bron/arsene-logo.ai`; de SVG's maak je met `python3 scripts/build-logos.py` (vereist `pymupdf`).
- Het brand book zelf is de SvelteKit-app in `src/` (tekst in `src/lib/content.ts`, pagina's in `src/lib/components/Page*.svelte`) en gebruikt dezelfde tokens. Een regel aanpassen? Doe het in `design-system/` én in het brand book, en draai daarna `yarn export:pdf` voor `arsene-huisstijl.pdf`.
- Een nieuwe component: map `design-system/components/<Naam>/` met `README.md` en `preview.html` (eerste regel `<!-- @dsCard group="..." height=... -->`), gedeelde CSS in `bundle.css` met prefix `ar-`, daarna `yarn tokens`.
