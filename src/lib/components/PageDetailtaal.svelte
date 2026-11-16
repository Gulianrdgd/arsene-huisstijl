<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="06 · Detailtaal" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Detailtaal.</h2>
        <p class="lede text-[12pt] leading-normal text-warm-800 mt-[6mm]">Kleine elementen die steeds terugkomen: de pin, de marker, de sectienummers en de knop. Gebruik ze met mate, het moet geen stickeralbum worden.</p>
      </div>
    </div>

    <div class="detail-grid" style="row-gap:10mm;">
      <!-- De pin -->
      <div class="grid gap-[3mm] content-start">
        <div class="flex justify-between items-baseline border-t border-ink pt-[3mm]">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">De pin</div>
          <div class="meta">Mint, minimaal 6 px</div>
        </div>
        <div class="min-h-[28mm] grid place-items-center rounded-sm bg-teal-deep">
          <div class="inline-flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-mint inline-block" style="box-shadow:0 0 14px #00b585;"></span>
            <span class="font-mono text-[10pt] tracking-[0.06em] text-teal-fg">live · uptime 99.98%</span>
          </div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Het teken dat we leven. Gebruik hem in statusregels, voor on-states en als scheidingsteken tussen mono-labels. Glow alleen op donker.</div>
      </div>

      <!-- Marker -->
      <div class="grid gap-[3mm] content-start">
        <div class="flex justify-between items-baseline border-t border-ink pt-[3mm]">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Marker</div>
          <div class="meta">Mint Bright</div>
        </div>
        <div class="min-h-[28mm] grid place-items-center rounded-sm bg-warm-200">
          <div class="font-sans text-[18pt] font-bold tracking-[-0.03em] text-ink">Software op <span class="mark">jouw voorwaarden</span>.</div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Een hoogtepunt op één of twee woorden per blok. Nooit op een hele zin. Bandhoogte ≈ 36% van de regelhoogte, onderaan uitgelijnd.</div>
      </div>

      <!-- Sectienummers -->
      <div class="grid gap-[3mm] content-start">
        <div class="flex justify-between items-baseline border-t border-ink pt-[3mm]">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Sectienummers</div>
          <div class="meta">Mono, twee cijfers</div>
        </div>
        <div class="min-h-[28mm] grid place-items-center rounded-sm bg-warm-200">
          <div class="font-mono text-[9pt] tracking-[0.08em] text-warm-600 inline-flex items-baseline gap-[8mm]">
            <span>01</span><span>02</span><span class="text-ink font-medium">03</span><span>04</span><span>05</span>
          </div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Altijd twee cijfers. Niet 1 maar 01. Op een lijn, gescheiden door witruimte. De huidige sectie staat in Ink.</div>
      </div>

      <!-- Knop -->
      <div class="grid gap-[3mm] content-start">
        <div class="flex justify-between items-baseline border-t border-ink pt-[3mm]">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Knop</div>
          <div class="meta">Teal Deep, 6 px radius</div>
        </div>
        <div class="min-h-[28mm] grid place-items-center rounded-sm bg-warm-200">
          <span class="inline-flex items-center gap-2 px-4 py-2.25 rounded-sm font-sans font-semibold text-[11pt] bg-teal-deep text-teal-fg">Begin een gesprek →</span>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Strakke, bijna haakse hoeken (6 px), zonder schaduw of gradient. Hover: ink. Outline-variant: 1.5 px boord, ink-kleur.</div>
      </div>
    </div>
  </div>
  <PageFoot page="08 / 11" />
</section>
