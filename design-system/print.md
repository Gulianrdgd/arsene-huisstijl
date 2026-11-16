# Print en documenten

A4-documenten (rapporten, offertes, handleidingen) volgen het brand book in deze repo: dat is zelf een A4-document en het beste voorbeeld. Bouw je een document in HTML, gebruik dan dezelfde aanpak: elke pagina is een `<section class="page">` van 210 × 297 mm en de export naar PDF loopt via headless Chromium (`npm run export:pdf`, zie `scripts/export-pdf.mjs`).

## Pagina

- A4 staand. Marges links en rechts `page-margin` (18 mm).
- Lopende kop op `page-head-top` (10 mm): het woordmerk links (Geist 600, 14 pt, met de pin), de sectie rechts in `print-running` ("03 · KLEUR").
- Inhoud van `page-body-top` (22 mm) tot 18 mm boven de onderkant.
- Paginanummer rechtsonder in `print-running` ("05 / 11"), `page-foot-bottom` (10 mm) van de onderkant. Geen documenttitel in de voet.
- Grond `paper`. Een slot- of colofonpagina mag volledig `teal-deep`.

## Opbouw van een sectie

1. Titel in `print-title` (48 pt, 700), eindigt met een punt.
2. Lede in `print-lede` (12 pt, `warm-800`), maximaal 140 mm breed, 6 mm onder de titel.
3. Inhoud in een raster van twee (soms vier) kolommen, 6 mm tussenruimte (`gap`).

## Omslag

Woordmerk linksboven, de titel groot in `print-cover` (112 pt) met de marker op één lettergreep of woord, een korte lede eronder, en onderaan links "Arsene" en rechts de datum in `print-running`.

## Inhoudsopgave

Een titel links, rechts een lijst met per regel het sectienummer (twee cijfers, Geist Mono, `warm-600`), de titel en het paginanummer, gescheiden door haarlijnen in `warm-400`.

## Export

- Gebruik geen box-shadow met blur en geen gradients met transparante stops: die exporteren als vlakken. De marker wordt in print een effen band (zie `@media print` in `src/routes/layout.css`).
- Fonts zelf hosten (`design-system/fonts/`), anders verdwijnt tekst in de PDF.

## Office-sjablonen

In `templates/`, gemaakt door `scripts/build-office.py` uit de tokens. Pas ze aan in dat script, niet met de hand.

| Sjabloon | Voor |
| --- | --- |
| `Arsene_document.dotx` | Rapport, offerte, notitie, handleiding |
| `Arsene_brief.dotx` | Brief |
| `Arsene_presentatie.potx` | Presentatie 16:9, met een voorbeelddia per layout |

**Eerst de fonts.** Installeer de statische fonts uit `fonts/geist/` en `fonts/geist-mono/`. Office zoekt naar "Geist", "Geist SemiBold" en "Geist Mono"; de variabele Geist alleen is niet genoeg.

**Word.**
- A4, marges 18 mm, lopende kop met het woordmerk links en de titel van het hoofdstuk rechts (veld STYLEREF op Kop 1), paginanummer rechtsonder als "05 / 11".
- Stijlen: Title (omslag, 40 pt), Intro (lede, 12 pt), Kop 1 (26 pt, eindigt met een punt), Kop 2 (13 pt SemiBold met een lijn erboven), Kop 3 (10 pt SemiBold), Normal (10 pt, Warm 800), Caption (8,5 pt, Warm 600), Lijstopsommingsteken, en de tabelstijl "Arsene tabel".
- Witte pagina's: kantoorprinters drukken geen paper-tint tot de rand. Paper is voor schermen en PDF's uit het brand book.
- De themakleuren zijn de grafiekkleuren: accent 1 tot 4 Mint Deep, oker, leiblauw, Mint; accent 5 warm grijs (context), accent 6 Warm 800.

**PowerPoint.**
- Layouts: Titel, Sectie, Titel en inhoud, Twee kolommen, Vergelijking, Statement, Alleen titel, Leeg, Afsluiting.
- Titel, Sectie en Afsluiting zijn `teal-deep` met het woordmerk in paper linksboven; de rest is paper met het woordmerk linksonder.
- Kop- en voettekst (Invoegen, Koptekst en voettekst): de voettekst staat linksboven in Geist Mono-kapitalen ("PROJECT · NAAM"), het dianummer rechtsboven, de datum rechtsonder. Zo staat het in de slide-mock van het brand book.
- Nadruk op één woord: kleur het in `mint-bright` op teal, of zet het in een eigen regel. Geen vet in lopende tekst.
