<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { taglines } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="08 · Taglines" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Taglines.</h2>
        <p class="lede text-[12pt] leading-normal text-warm-800 mt-[6mm]">Elke tagline draagt één boodschap. Kies per context de tagline die past, en gebruik ze niet allemaal door elkaar.</p>
      </div>
    </div>

    <div class="tag-grid">
      {#each taglines as card (card.nl)}
        <div class="border-t border-ink pt-[5mm] pb-[2mm]">
          <div class="text-[26pt] leading-none tracking-[-0.045em] font-bold text-ink mb-[3mm]" style="white-space:pre-line;">{card.nl}</div>
          <div class="text-[11pt] italic tracking-[-0.01em] text-warm-800 mb-[3mm]">{card.en}</div>
          <div class="text-[8.5pt] leading-normal text-warm-600">{card.note}</div>
        </div>
      {/each}
    </div>
  </div>
  <PageFoot page="10 / 11" />
</section>
