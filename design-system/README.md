# Arsene design system

Arsene is een Nederlandse IT-consultancy voor het MKB. De huisstijl is warm papier, diep teal en één mintgroene punt: de pin. Hij is rustig en droog, en laat het werk spreken.

Deze pagina geeft de basis. Schrijven staat in `schrijven.md`, websites in `web.md`, A4-documenten in `print.md`, de details per bouwsteen in `components/`. Het brand book in `src/` (de SvelteKit-app, export naar `arsene-huisstijl.pdf`) bevat dezelfde regels; pas een regel altijd op beide plekken aan. Twijfel je of iets past? Maak het soberder.

## Kleur

Alle waarden en het contrast per kleur staan in `tokens.json`. Verzin geen kleuren, ook geen tinten of transparanties die daar niet staan.

- **Paper** (`paper`) is de grond van alles. Tekst erop is `ink`, secundaire tekst `warm-800`.
- **Teal** (`teal-deep`, `teal-card`) geeft gewicht: knoppen, slides, het colofon, een hero. Tekst op teal is `teal-fg`; secundair op 70% dekking, metadata op 55%, lijnen op 18%.
- **Mint** (`mint`) is het signaal en verschijnt bijna alleen als de pin. Nooit als tekstkleur op paper. Op een mint vlak staat alleen `teal-deep` tekst, nooit wit.
- **Mint Bright** (`mint-bright`) is de marker achter één of twee woorden. Op teal wordt het de tekstkleur van het benadrukte woord.
- **Signal** (`signal`) is voor fouten, waarschuwingen en de Niet doen-tag. Spaarzaam.
- Drie families: paper draagt het beeld, teal en mint zijn accent. Geen gradients, geen schaduwen, geen pasteltinten buiten het palet.
- Op het web gebruik je de rollen `web-*` (licht en donker, zie `web.md`).

## Lettertypen

- **Geist** voor alles: koppen, tekst, knoppen. Gewichten 400 (tekst), 500, 600 (labels, kleine koppen, het woordmerk) en 700 (titels).
- **Geist Mono** voor metadata: lopende kop en paginanummer, hex-waarden, maten, code, tags. Gewichten 400 tot 600.
- Grote titels spatiëren negatief (−0,035 tot −0,05 em, zie de tokens) en eindigen in print met een punt: "Kleur.", "Tot zover.".
- Webfonts staan in `fonts/` (OFL, zie `licenses/`). Host ze zelf, geen Google Fonts.

## Rangorde

| Rol | Web | Print (A4) | Vorm |
| --- | --- | --- | --- |
| Display | 84 px (`web-display-2xl`), 64 px (`web-display-xl`) | 112 pt omslag (`print-cover`) | 700, `ink` |
| Titel, h1 | 44 px (`web-heading-1`) | 48 pt (`print-title`) | 700, eindigt met een punt in print |
| h2 | 32 px (`web-heading-2`) | 13 pt blokkop (`print-heading`) | 600 |
| Lede | 20 px (`web-lede`) | 12 pt (`print-lede`) | 400, secundaire tekstkleur, max. 65 tekens of 140 mm |
| Tekst | 16 px (`web-body`) | 10 pt (`print-body`) | 400 |
| Label | | 9,5 pt (`print-label`) | 600, zinsvorm, `ink` |
| Meta | | 8,5 pt (`print-meta`) | 400, zinsvorm, `warm-600` |
| Lopende kop | | 8 pt (`print-running`) | Geist Mono, kapitalen, +0,08 em |

- **Geen eyebrow of kopregel.** Arsene zet geen klein label in kapitalen boven een titel. Een groep krijgt hooguit een label in zinsvorm.
- **Zinsvorm overal**, ook in titels. Kapitalen alleen in Geist Mono voor korte metadata: lopende kop, paginanummer, tags.
- Meta en specificaties in zinsvorm ("Teal Deep, 6 px radius"), niet als `TEAL DEEP · 6PX RADIUS`.

## Logo

- Het **woordmerk** is "arsene" in kleine letters, Geist 600, −4% spatiëring, met de pin erachter. Bestanden: `assets/logo/arsene-wordmark-ink.svg` (op licht) en `arsene-wordmark-paper.svg` (op teal of een foto).
- Het **beeldmerk** is de a met de pin (`arsene-mark-ink.svg`, `-paper.svg`), voor plekken die te klein zijn voor het woordmerk. Als app-icoon en favicon het teal vierkant met afgeronde hoeken (18%): `arsene-icon.svg`.
- Altijd het bestand gebruiken. Niet zelf zetten, uitrekken, herkleuren of in kapitalen. De pin blijft mint.
- Clearspace: minstens één pin-breedte aan alle zijden. Niet op drukke achtergronden.
- Maten: groot (36 pt print, hero en omslag, pin met glow), medium (22 pt, navigatie en signature), klein (14 pt, visitekaartje en voetnoten, pin zonder glow). Glow alleen op donker.
- De bron is `assets/logo/bron/arsene-logo.ai`. De SVG's maak je opnieuw met `python3 scripts/build-logos.py`.

## Detailtaal

Vier kleine elementen die steeds terugkomen. Gebruik ze met mate.

- **De pin**: het mintgroene punt. Het teken dat we leven: in statusregels, voor on-states, als scheidingsteken tussen mono-labels.
- **De marker**: een band in `mint-bright` achter één of twee woorden per blok, nooit een hele zin. Bandhoogte ongeveer 36% van de regelhoogte, onderaan.
- **Sectienummers**: altijd twee cijfers (01, niet 1), in Geist Mono. De huidige sectie staat in `ink`, de rest in `warm-600`.
- **De knop**: `teal-deep` met `teal-fg` tekst, 6 px radius, geen schaduw of gradient. Hover `ink`. Outline-variant: 1,5 px rand in `ink`.

## Vorm

- Weinig kaders. Een blok begint met een dunne lijn in `ink` (1 px) erboven, dan de kop, dan de inhoud. Gebruik een vlak (`warm-200`, 4 px radius) alleen waar een voorbeeld of demo een eigen ondergrond nodig heeft.
- Geen schaduwen, geen gradients, geen pillen. Tags hebben 1 mm radius.
- Doe dit en Niet doen: een tag in Geist Mono-kapitalen. Doe dit is mint met `teal-deep` tekst, Niet doen een rand en tekst in `signal`.
- Veel witruimte. Liever een lege onderkant dan een volle pagina.

## Componenten

Elke component heeft in `components/` een `README.md` met de regels en een `preview.html`. Gedeelde CSS staat in `components/bundle.css`, alle voorbeelden samen in `index.html` (open via een lokale server, bijvoorbeeld `python3 -m http.server` in de repo-root).

- **Merk**: Woordmerk, Beeldmerk, Iconen.
- **Detail**: Pin, Marker, Sectienummers, Knop, Tag.
- **Tekst**: Sectiekop, LabelEnMeta, Blok.
- **Data**: Grafiek, Tabel.
- **Web**: Kopbalk, Hero, Websitefooter.
- **Print**: Pagina.
- **Toepassingen**: Emailhandtekening, Visitekaartje.

## Iconen

Phosphor Icons, gewicht Regular, in `assets/icons/` (MIT). Liever tekst dan een icoon; 16 tot 24 px; altijd in de tekstkleur, nooit mint. Zie `components/Iconen`.

## Grafieken

Bij voorkeur één reeks uitgelicht in `chart-1` (Mint Deep) en de rest in warm grijs (`chart-context`), zodat mint het signaal blijft. Meer reeksen: `chart-1` tot `chart-4` in vaste volgorde (Mint Deep, oker, leiblauw, Mint); oker en leiblauw bestaan alleen voor grafieken. Gevalideerd op kleurenblindheid en contrast, in licht en donker. Zie `components/Grafiek`.

## Office

Sjablonen voor Word en PowerPoint staan in `templates/` (zie `print.md`). Installeer eerst Geist en Geist Mono uit `fonts/`.

## Wat nog niet vastligt

Fotografie en illustratie heeft het brand book nog niet. Verzin er geen stijl voor; vraag het na bij brand@arsene.nl of houd het sober.

Iconen, grafieken, de website-footer en de Office-sjablonen zijn later toegevoegd en volgen uit de bestaande regels. Ze staan nog niet in het brand book zelf.
