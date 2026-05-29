<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { colorGroups } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="03 · Kleur" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Kleur.</h2>
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">Warm papier als basis, diepteal voor gewicht, mint als signaal. Drie families — meer is bijna nooit nodig.</p>
      </div>
    </div>

    {#each colorGroups as row (row.label)}
      <div class="mb-[6mm]">
        <div class="font-mono text-[8pt] tracking-widest uppercase text-warm-600 mb-[3mm]">{row.label}</div>
        <div class="palette">
          {#each row.swatches as s (s.name)}
            <div class="swatch rounded-sm overflow-hidden border border-warm-400 bg-surface">
              <div class="chip w-full" style="background:{s.bg};"></div>
              <div class="p-[3mm_3.5mm_4mm] grid gap-[1.2mm]">
                <div class="text-[10pt] font-semibold tracking-[-0.01em] text-ink">{s.name}</div>
                <div class="font-mono text-[8.5pt] text-warm-800 tracking-[0.02em]">{s.hex}</div>
                <div class="font-mono text-[7.5pt] text-warm-600 tracking-[0.02em]">{s.rgb}</div>
                <div class="text-[8pt] leading-[1.4] text-warm-600 mt-[0.5mm]">{s.role}</div>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/each}

    <div class="text-[8.5pt] leading-normal text-warm-600 mt-[4mm]">
      Paper draagt het beeld; teal en mint zijn accent. Mint mag op paper en op teal; op mint zelf alleen teal-tekst. Geen gradients, geen pasteltinten buiten dit palet.
    </div>
  </div>
  <PageFoot page="05 / 11" />
</section>
