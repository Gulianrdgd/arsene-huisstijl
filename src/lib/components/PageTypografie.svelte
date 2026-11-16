<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { typeScale } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="04 · Typografie" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Typografie.</h2>
        <p class="lede text-[12pt] leading-normal text-warm-800 mt-[6mm]">Geist voor het werk, Geist Mono voor bijschriften en metadata. Beide hebben dezelfde heldere, wat mechanische toon.</p>
      </div>
    </div>

    <div class="type-pair mb-[4mm]">
      <div class="border-t border-ink pt-[4mm]">
        <div class="label text-warm-600 mb-[1mm]">Primair</div>
        <div class="text-[16pt] font-semibold tracking-[-0.02em] mb-[4mm] text-ink">Geist</div>
        <div class="text-[28pt] tracking-[-0.02em] leading-none mb-[2mm] text-ink">AaBb 0123</div>
        <div class="text-[9pt] text-warm-800 mb-[3mm] tracking-[0.02em]">abcdefghijklmnopqrstuvwxyz</div>
        <div class="text-[8.5pt] leading-normal text-warm-600">Alle gewichten 300–900. Sans-serif met scherpe terminals. Voor headlines, body, UI.</div>
      </div>
      <div class="border-t border-ink pt-[4mm]">
        <div class="label text-warm-600 mb-[1mm]">Detail</div>
        <div class="font-mono text-[16pt] font-semibold tracking-[-0.02em] mb-[4mm] text-ink">Geist Mono</div>
        <div class="font-mono text-[28pt] leading-none mb-[2mm] font-medium text-ink">AaBb 0123</div>
        <div class="font-mono text-[9pt] text-warm-800 mb-[3mm]">abcdef · 12345 · ··-→</div>
        <div class="text-[8.5pt] leading-normal text-warm-600">Gewichten 400/500/600. Voor metadata, codetekst en sectienummers.</div>
      </div>
    </div>

    <div class="h-px bg-warm-400 my-[6mm]"></div>

    <h3 class="label mb-[5mm]">Schaal</h3>
    <div class="flex flex-col gap-[4mm]">
      {#each typeScale as row (row.label)}
        <div class="type-row border-t border-warm-400 pt-[3mm]">
          <div class="meta">{row.label}</div>
          <div class="font-sans text-ink" style={row.style}>{row.text}</div>
          <div class="font-mono text-[8pt] text-warm-600 text-right">{row.meta}</div>
        </div>
      {/each}
    </div>
  </div>
  <PageFoot page="06 / 11" />
</section>
