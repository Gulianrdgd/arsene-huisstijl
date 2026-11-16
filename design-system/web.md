# Web

Websites en webapps volgen het brand book. Link `tokens.css` en `components/bundle.css`, gebruik de kleurrollen `web-*` en de tekststijlen `web-*`. De bouwstenen (Kopbalk, Hero, Knop, Blok, Footer) staan met hun maten in `components/`.

```html
<link rel="preload" href="/design-system/fonts/geist-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/design-system/tokens.css">
<link rel="stylesheet" href="/design-system/components/bundle.css">
```

Het brand book is gemaakt voor print. Waar het voor het web niets zegt (donkere modus, links, focus, navigatie, status, kleine tekstmaten) staan hier voorstellen die uit de bestaande regels volgen. Ze zijn gemarkeerd met *voorstel*; pas ze aan zodra het brand book ze vastlegt.

In een Tailwind v4-project importeer je `tokens.css` en koppel je de kleuren in `@theme inline` (zie `src/routes/layout.css` in deze repo als voorbeeld). Gebruik de tokennamen, geen losse hex-waarden.

## Pagina

- Grond `web-background` (paper), tekst `web-text` (ink). Breedte maximaal `web-grid` (1440 px).
- Lopende tekst en ledes maximaal 65 tekens breed. Koppen mogen breder.
- Veel witruimte tussen secties. Een sectie begint met een titel en een lede, dan de inhoud.
- Blokken naast elkaar beginnen met een dunne lijn in `web-rule` (1 px) erboven, geen kaart met rand en schaduw.
- Favicon en app-icoon: `assets/logo/arsene-icon.svg`. `theme-color` is `#f4f1e8` in licht en `#06120f` in donker.

## Licht en donker (donker is een *voorstel*)

Licht is het palet van het brand book. Donker is afgeleid van de teal-pagina's (colofon, slides); het brand book legt nog geen donkere modus vast.

- Zet `data-theme="light"` of `"dark"` op `<html>`; zonder attribuut volgt de pagina `prefers-color-scheme`. Een schakelaar onthoudt de keuze en past hem toe voordat de pagina tekent.
- Donker: grond `teal-deep`, vlakken `teal-card`, tekst `teal-fg`. Het woordmerk wordt `arsene-wordmark-paper.svg`.
- De marker is in donker geen band maar de tekstkleur `mint-bright`.
- De knop is in donker mint met `teal-deep` tekst.

## Links en knoppen

De knop komt uit het brand book; links en focus zijn een *voorstel*.

- **Links** in lopende tekst: tekstkleur `web-link`, onderstreept met 1 px in `web-link-underline`, 0,2 em onder de basislijn. Onder de muis wordt de onderstreping 2 px. Een link is het onderwerp, nooit "klik hier".
- **Primaire knop**: `web-button` met `web-button-text`, Geist 600, 6 px radius (`radius-button`), binnenmarge 0,6 × 1 em. Hover `ink` (licht). Geen schaduw, geen gradient. Een pijl → mag achter de tekst.
- **Secundaire knop**: transparant, rand 1,5 px in `web-text`, tekst `web-text`.
- Focus: een omlijning van 2 px in `web-text` met 2 px afstand. Nooit weghalen.

## Navigatie

Afgeleid van de site-mock in het brand book; de actieve staat is een *voorstel*.

- Kopbalk: woordmerk links (medium), navigatie rechts in Geist Mono-kapitalen, klein, `web-text-muted`, met een haarlijn `web-line` eronder. De actieve pagina in `web-text` met de pin ervoor.
- Kort houden: drie tot vijf items.

## Toegankelijkheid

- Kleine tekst haalt minstens 4,5:1. Daarom op het web nooit `warm-600` als tekstkleur (3,0:1 op paper); `web-text-muted` is `warm-800` (7,8:1).
- `mint` is geen tekstkleur op paper (2,3:1). `mint-deep` als tekst alleen groot of vet (4,4:1); voor links is het de onderstreping, niet de tekst.
- `signal` op paper haalt 4,1:1: foutmeldingen krijgen een vette titel en een rand in `signal`, de uitleg in `web-text`.
- Animaties uit bij `prefers-reduced-motion`. De glow rond de pin is statisch, geen puls.

## Status (*voorstel*)

De pin is ook de statusindicator: een mint punt voor "live" of "aan". Glow alleen op een donkere grond. Uit of offline is `warm-400` zonder glow. Fouten krijgen `signal` en tekst erbij, nooit alleen een kleur.
