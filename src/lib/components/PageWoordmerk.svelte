<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { anatomyItems, wordmarkSizes } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="01 · Woordmerk" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Woordmerk.</h2>
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">Eén woord, kleine letters, een muntgroene punt. Het hele merk komt samen in dit teken: de naam zonder kapsones, en die ene <span class="mark">pin</span> als signaal dat we nog leven.</p>
      </div>
    </div>

    <div class="logo-hero bg-teal-deep text-teal-fg rounded-sm relative grid place-items-center mb-[8mm]">
      <div class="corner font-mono text-[8pt] tracking-widest text-[rgba(217,232,228,0.55)] uppercase">Primair · op Teal Deep</div>
      <span class="wordmark wordmark--xxl font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-teal-fg">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
    </div>

    <div class="anatomy mb-[6mm]">
      {#each anatomyItems as [k, v] (k)}
        <div class="border-t border-warm-400 pt-[3mm]">
          <div class="font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600 mb-[1mm]">{k}</div>
          <div class="text-[10pt] leading-[1.4] text-ink">{v}</div>
        </div>
      {/each}
    </div>

    <div class="h-px bg-warm-400 mb-[6mm]"></div>

    <div class="grid gap-[6mm] items-end" style="grid-template-columns:1fr 1fr 1fr;">
      {#each wordmarkSizes as { cls, label, note } (cls)}
        <div>
          <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[4mm]">{label}</div>
          <span class="wordmark {cls} font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
          <div class="text-[8.5pt] leading-normal text-warm-600 mt-[3mm]">{note}</div>
        </div>
      {/each}
    </div>
  </div>
  <PageFoot page="03 / 11" />
</section>
