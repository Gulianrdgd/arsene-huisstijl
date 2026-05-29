<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { toneRules, voiceExamples } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="05 · Toon &amp; taal" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Toon &amp; taal.</h2>
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">We schrijven zoals we praten — droog, concreet, een tikje Nederlands. We schoppen niet, maar we vermijden ook het lege galmen van het consultancy-vocabulaire.</p>
      </div>
    </div>

    <div class="grid gap-[6mm] mb-[8mm]" style="grid-template-columns:1fr 1fr 1fr;">
      {#each toneRules as [label, text] (label)}
        <div>
          <div class="font-mono text-[8pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[2mm]">{label}</div>
          <div class="text-[8.5pt] leading-normal text-warm-600">{text}</div>
        </div>
      {/each}
    </div>

    <div class="flex flex-col gap-0">
      {#each voiceExamples as item (item.nl)}
        <div class="voice-item border-t border-warm-400 py-[4mm] {item.do ? '' : 'voice-dont'}">
          <div>
            {#if item.do}
              <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center">Doe dit</span>
            {:else}
              <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center border border-signal text-signal text-center">Niet doen</span>
            {/if}
          </div>
          <div>
            <div class="quote text-[13pt] leading-[1.4] tracking-[-0.005em] text-ink mb-[1.5mm]">{item.nl}</div>
            <div class="text-[9pt] text-warm-600 italic">{item.en}</div>
          </div>
        </div>
      {/each}
    </div>
  </div>
  <PageFoot page="07 / 11" />
</section>
