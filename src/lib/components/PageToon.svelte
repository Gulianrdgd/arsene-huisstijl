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
        <p class="lede text-[12pt] leading-normal text-warm-800 mt-[6mm]">We schrijven zoals we praten: droog, concreet en een tikje Nederlands. We schoppen niet tegen anderen aan en laten het holle consultancy-jargon liggen.</p>
      </div>
    </div>

    <div class="grid gap-[6mm] mb-[8mm]" style="grid-template-columns:1fr 1fr 1fr;">
      {#each toneRules as [label, text] (label)}
        <div>
          <div class="label mb-[1.5mm]">{label}</div>
          <div class="text-[8.5pt] leading-normal text-warm-800">{text}</div>
        </div>
      {/each}
    </div>

    <div class="flex flex-col gap-0">
      {#each voiceExamples as item (item.nl)}
        <div class="voice-item border-t border-warm-400 py-[4mm] {item.do ? '' : 'voice-dont'}">
          <div>
            {#if item.do}
              <span class="tag tag--do">Doe dit</span>
            {:else}
              <span class="tag tag--dont">Niet doen</span>
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
