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
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">Kleine terugkerende elementen die het beeld dragen: de marker, de pin, het eyebrow-label, de sectienummers. Gebruik ze met mate, niet als sticker-album.</p>
      </div>
    </div>

    <div class="detail-grid">
      <!-- Marker -->
      <div class="bg-surface border border-warm-400 rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Marker</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600">accent · mint bright</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
          <div class="font-sans text-[18pt] font-bold tracking-[-0.03em] text-ink">Software op <span class="mark">jouw voorwaarden</span>.</div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Een hoogtepunt op één of twee woorden per blok. Nooit op een hele zin. Bandhoogte ≈ 36% van de regelhoogte, onderaan uitgelijnd.</div>
      </div>

      <!-- De pin -->
      <div class="bg-teal-deep border-teal-deep rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-teal-fg">De pin</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-[rgba(217,232,228,0.55)]">mint · ≥ 6 px</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center rounded-[3px] bg-[rgba(255,255,255,0.04)]">
          <div class="inline-flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-mint inline-block" style="box-shadow:0 0 14px #00b585;"></span>
            <span class="font-mono text-[10pt] tracking-[0.06em] text-teal-fg">live · uptime 99.98%</span>
          </div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-[rgba(217,232,228,0.7)]">Het signaal "we leven". Gebruik in statusrijtjes, on-states, en als losse interpunctie tussen mono-labels. Glow alleen op donker.</div>
      </div>

      <!-- Eyebrow-label -->
      <div class="bg-surface border border-warm-400 rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Eyebrow-label</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600">mono · 0.14em · upper</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
          <div class="font-mono text-[10pt] tracking-[0.16em] uppercase text-mint-deep font-medium">— 03 · Kleur</div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Mono, uppercase, met em-dash ervoor of het sectienummer. Altijd Mint Deep op paper, Mint Bright op teal.</div>
      </div>

      <!-- Sectienummers -->
      <div class="bg-surface border border-warm-400 rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Sectienummers</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600">mono · 2-digit</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
          <div class="font-mono text-[9pt] tracking-[0.08em] text-warm-600 inline-flex items-baseline gap-[8mm]">
            <span>01</span><span>02</span><span class="text-ink">— 03</span><span>04</span><span>05</span>
          </div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Altijd twee cijfers. Niet 1 maar 01. Op een lijn, gescheiden door witruimte. De huidige sectie krijgt een em-dash ervoor.</div>
      </div>

      <!-- Knop -->
      <div class="bg-surface border border-warm-400 rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Knop</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600">teal deep · 6px radius</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
          <span class="inline-flex items-center gap-2 px-4 py-2.25 rounded-sm font-sans font-semibold text-[11pt] bg-teal-deep text-teal-fg">Begin een gesprek →</span>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Strak, bijna haakse hoeken (6 px). Geen schaduw, geen gradient. Hover: ink. Outline-variant: 1.5 px boord, ink-kleur.</div>
      </div>

      <!-- Em-dash -->
      <div class="bg-surface border border-warm-400 rounded-sm p-[6mm] grid gap-[4mm]">
        <div class="flex justify-between items-baseline">
          <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Em-dash</div>
          <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600">— · niet -</div>
        </div>
        <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
          <div class="text-[16pt] font-medium tracking-[-0.01em] text-ink">Klein bedrijf — echte infrastructuur.</div>
        </div>
        <div class="text-[9pt] leading-[1.45] text-warm-800">Het em-dash (—) is het Arsene-leesteken bij uitstek. Spatie ervoor en erna. Geen hyphens, geen ndashen voor losse pauzes.</div>
      </div>
    </div>
  </div>
  <PageFoot page="08 / 11" />
</section>
