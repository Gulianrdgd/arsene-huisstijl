Grafieken in de huisstijl. Kleuren in `tokens.json` onder `color.chart`, gevalideerd op kleurenblindheid en contrast op `paper` en `teal-deep`.

**Eerst de vorm.** Eén getal is geen grafiek: zet het groot neer. Vergelijk je grootheden, gebruik staven; verloop in de tijd, een lijn. Nooit taart- of donutdiagrammen met meer dan twee delen, nooit 3D, nooit twee y-assen.

**Kleur.**
- Voorkeur: één reeks uitgelicht in `chart-1`, de rest in `chart-context` (warm grijs). Zo werkt mint als signaal, zoals de pin.
- Meer reeksen: `chart-1` tot `chart-4` in die volgorde, nooit cyclisch, nooit herordend als een filter reeksen weghaalt. Oker (`chart-2`) en leiblauw (`chart-3`) zijn alleen voor grafieken.
- Lijnen, staven en stapels maximaal 4 reeksen; spreidingsdiagrammen en small multiples maximaal 3. Meer? Voeg samen tot "Overig" of maak kleine grafieken naast elkaar.
- Intensiteit (heatmap, kaart): de schaal `chart-seq-1` tot `-5`, één tint mint.
- `signal` is geen reekskleur; alleen voor een fout of overschrijding, met tekst erbij.
- `chart-2` en `chart-4` halen minder dan 3:1 op paper: altijd directe labels of de tabel.

**Vorm.**
- Staven maximaal 24 px breed, bovenkant 4 px afgerond, onderkant recht op de basislijn.
- Lijnen 2 px, eindpunt 8 px met een ring van 2 px in de achtergrondkleur.
- Rasterlijnen 1 px, doorgetrokken, in `chart-grid`. Asteksten in Geist Mono 11 px, `web-text-muted`, ronde getallen.
- Een legenda bij twee of meer reeksen, plus directe labels aan het eind van de lijn of op de hoogste staaf. Nooit een getal bij elk punt.
- Tekst draagt nooit de reekskleur: labels en waarden in `web-text`, de kleur zit in het streepje ernaast.
- Titel in zinsvorm boven de grafiek, met eronder de bron of toelichting in `ar-meta`.

**Interactie en toegankelijkheid.**
- Op het web altijd een tooltip bij hover (kruisdraad bij lijnen), en een tabelweergave (`details` met `ar-table`).
- `role="img"` met een `aria-label` die de conclusie noemt.
- In Office: de themakleuren van de sjablonen volgen dezelfde volgorde (accent 1 tot 4).
