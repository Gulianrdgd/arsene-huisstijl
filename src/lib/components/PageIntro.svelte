<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
  import { tocItems } from '$lib/content';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="Inleiding · Inhoud" />
  <div class="page__body">
    <div class="toc">
      <div>
        <h2 class="text-[36pt] leading-[0.98] tracking-[-0.04em] font-bold text-ink mb-[8mm]">Een<br/>handleiding<br/>met ruimte.</h2>
        <div class="text-[11pt] leading-[1.55] text-warm-800 flex flex-col gap-[4mm]">
          <p>Dit is de huisstijl van Arsene. Hij zorgt dat alles wat we maken herkenbaar is en bij elkaar past, zonder het werk in de weg te zitten.</p>
          <p>Deze gids beschrijft de bouwstenen (logo, kleur, typografie en toon) en hoe ze samenhangen. Templates staan er niet in. Binnen deze regels verwachten we dat je zelf keuzes maakt.</p>
          <p>Twijfel je of iets past? Maak het dan soberder. Arsene draait om rust en duidelijkheid.</p>
        </div>
      </div>
      <div>
        <h3 class="label mb-[4mm] pt-[3mm]">Inhoud</h3>
        <ol class="list-none p-0 flex flex-col gap-[1mm]">
          {#each tocItems as { n, title, page } (n)}
            <li class="border-b border-warm-400 text-[11pt] py-[2mm]">
              <span class="font-mono text-[9pt] text-warm-600 tracking-[0.06em]">{n}</span>
              <strong class="font-medium tracking-[-0.01em]">{title}</strong>
              <span class="font-mono text-[9pt] text-warm-600">{page}</span>
            </li>
          {/each}
        </ol>
      </div>
    </div>
  </div>
  <PageFoot page="02 / 11" />
</section>
