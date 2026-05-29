<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="02 · Beeldmerk &amp; clearspace" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Beeldmerk &amp; clearspace.</h2>
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">Voor favicons, avatars en alles wat te klein is voor de woordmerk: het teal-vierkant met de pin in het midden. Halo-ring komt mee, of niet — afhankelijk van de plek.</p>
      </div>
    </div>

    <div class="grid gap-[6mm] mb-[6mm]" style="grid-template-columns:1fr 1fr;">
      <!-- Do: clearspace -->
      <div class="swatch-card border border-warm-400 rounded-sm bg-surface">
        <div class="demo bg-paper relative grid place-items-center">
          <div class="brand-mark" style="width:38mm;font-size:28mm;border-radius:8mm;">
            <span class="glyph">a<span class="pin"></span></span>
          </div>
          <div class="absolute inset-0 pointer-events-none">
            <div class="absolute" style="left:22mm;right:22mm;top:4mm;height:2mm;border-left:1px solid #c1bba5;border-right:1px solid #c1bba5;"></div>
            <div class="absolute" style="top:22mm;bottom:22mm;left:4mm;width:2mm;border-top:1px solid #c1bba5;border-bottom:1px solid #c1bba5;"></div>
          </div>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center">Doe dit</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Houd minstens één pin-breedte clearspace aan alle zijden.</span>
        </div>
      </div>

      <!-- Do: proportional scaling -->
      <div class="swatch-card border border-warm-400 rounded-sm bg-surface">
        <div class="demo bg-paper flex items-center justify-center gap-[4mm]">
          <div class="brand-mark brand-mark--soft" style="width:22mm;font-size:16mm;border-radius:4mm;background-color:#06120f;">
            <span class="glyph">a<span class="pin"></span></span>
          </div>
          <div class="brand-mark brand-mark--soft" style="width:14mm;font-size:10mm;border-radius:3mm;background-color:#06120f;">
            <span class="glyph">a<span class="pin"></span></span>
          </div>
          <div class="brand-mark brand-mark--soft" style="width:8mm;font-size:5.8mm;border-radius:1.6mm;background-color:#06120f;">
            <span class="glyph">a<span class="pin"></span></span>
          </div>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center">Doe dit</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Schaal proportioneel. De pin blijft ¼ van het vierkant.</span>
        </div>
      </div>
    </div>

    <div class="dodont">
      <!-- Niet doen: stretchen -->
      <div class="swatch-card swatch-card--sm border border-warm-400 rounded-sm bg-surface">
        <div class="demo bg-paper grid place-items-center">
          <span class="stretched">arsene<span class="pin"></span></span>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Nooit horizontaal of verticaal stretchen.</span>
        </div>
      </div>
      <!-- Niet doen: verkeerde kleur pin -->
      <div class="swatch-card swatch-card--sm border border-warm-400 rounded-sm bg-surface">
        <div class="demo bg-paper grid place-items-center">
          <span class="wrong-color">arsene<span class="pin"></span></span>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Geen andere kleur voor de pin. Mint blijft mint.</span>
        </div>
      </div>
      <!-- Niet doen: drukke achtergrond -->
      <div class="swatch-card swatch-card--sm border border-warm-400 rounded-sm bg-surface">
        <div class="demo grid place-items-center" style="background: repeating-linear-gradient(45deg, rgba(0,0,0,0.06) 0 2px, transparent 2px 8px), #f4f1e8;">
          <span class="wordmark wordmark--lg font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Niet op drukke achtergronden. Houd het rustig.</span>
        </div>
      </div>
      <!-- Niet doen: kapitalen -->
      <div class="swatch-card swatch-card--sm border border-warm-400 rounded-sm bg-surface">
        <div class="demo bg-paper grid place-items-center">
          <span class="wordmark wordmark--lg font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink uppercase">ARSENE<span class="pin inline-block rounded-full bg-mint"></span></span>
        </div>
        <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
          <span class="font-mono text-[8pt] leading-none tracking-widest uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
          <span class="text-[9.5pt] leading-[1.35] text-warm-800">Nooit kapitalen. Het merk is consequent lowercase.</span>
        </div>
      </div>
    </div>
  </div>
  <PageFoot page="04 / 11" />
</section>
