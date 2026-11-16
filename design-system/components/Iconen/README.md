Iconen komen uit **Phosphor Icons**, gewicht **Regular** (MIT, zie `assets/icons/LICENSE-phosphor.txt`). De lijn past bij Geist: rond, gelijkmatig, niet te dun. Een selectie staat in `assets/icons/`.

- Liever tekst dan een icoon. Gebruik een icoon alleen waar het sneller leest dan een woord: navigatie, knoppen met een pijl, status, contactgegevens, een zoekveld.
- Maten 16, 20 en 24 px (in print 4 tot 6 mm). Niet groter: een groot icoon als illustratie hoort niet bij de stijl.
- Kleur `currentColor`: het icoon neemt de tekstkleur over (`web-text` of `web-text-secondary`). Nooit mint; mint is de pin.
- Inline als SVG (`fill="currentColor"` staat al in het bestand), zodat de kleur met het thema meegaat. In Office als SVG invoegen en herkleuren naar Ink.
- Altijd met tekst ernaast of een `aria-label`. Een icoon alleen is nooit de enige uitleg.
- Eén set, één gewicht. Geen andere sets, geen gevulde (fill) of duotone-varianten, geen emoji.
- Een pijl in een knop mag ook het tekstteken → zijn, zoals in het brand book.
- Mis je een icoon? Haal het uit Phosphor Regular (`@phosphor-icons/core`, map `assets/regular/`), zet het in `assets/icons/` en draai `yarn tokens` om dit overzicht bij te werken.
