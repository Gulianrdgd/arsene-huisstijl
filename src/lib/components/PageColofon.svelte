<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { colophonMeta } from '$lib/content';
</script>

<section class="page page--teal bg-teal-deep text-teal-fg relative overflow-hidden">
  <PageHead title="+ · Colofon" dark />
  <div class="page__body">
    <div class="colophon">
      <div class="head-block">
        <div>
          <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-bright mb-[6mm]">— Colofon</div>
          <h2 class="title-xl font-sans text-teal-fg">Tot zover.</h2>
          <p class="text-[12pt] leading-normal text-teal-fg opacity-[0.78] mt-[6mm]">Vragen, dubbelpunten, of een uiting die niet past in dit boekje? Stuur het op. We werken liever met je mee dan er omheen.</p>
        </div>
        <div class="brand-mark brand-mark--soft shrink-0" style="width:28mm;font-size:20mm;border-radius:5mm;">
          <span class="glyph">a<span class="pin"></span></span>
        </div>
      </div>

      <div class="w-full text-[10pt] leading-normal">
        {#each colophonMeta as [k, v] (k)}
          <div class="colophon meta-row border-t py-[3mm]" style="border-color:rgba(217,232,228,0.18);">
            <div class="font-mono text-[8.5pt] tracking-widest uppercase text-[rgba(217,232,228,0.55)]">{k}</div>
            <div class="text-teal-fg">{v}</div>
          </div>
        {/each}
      </div>

      <div class="closing font-sans text-teal-fg">
        alles<br/>kan<span class="closing-pin"></span>
      </div>
    </div>
  </div>
  <PageFoot page="11 / 11" dark />
</section>
