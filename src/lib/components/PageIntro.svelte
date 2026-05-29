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
        <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[8mm]">— Introductie</div>
        <h2 class="text-[36pt] leading-[0.98] tracking-[-0.04em] font-bold text-ink mb-[6mm]">Een handleiding,<br/>geen knellend keurslijf.</h2>
        <div class="text-[11pt] leading-[1.55] text-warm-800 flex flex-col gap-[4mm]">
          <p>Voor je ligt de huisstijl van Arsene. Het doel: in alles wat we maken een herkenbaar en samenhangend beeld neerzetten. Een huisstijl moet professioneel en consistent zijn, maar mag nooit het werk in de weg zitten.</p>
          <p>Deze gids beschrijft de bouwstenen — logo, kleur, typografie, toon — en hoe ze zich tot elkaar verhouden. Zie het niet als een verzameling templates. Het is een kader. Binnen dat kader is creativiteit niet alleen toegestaan, maar nodig.</p>
          <p>Twijfel je of iets binnen de stijl past? Doe het iets soberder. Arsene leunt op rust en duidelijkheid; niet op decoratie.</p>
        </div>
      </div>
      <div>
        <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[8mm]">— Inhoud</div>
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
