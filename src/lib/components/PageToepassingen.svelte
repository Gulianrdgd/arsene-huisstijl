<script lang="ts">
  import PageHead from './PageHead.svelte';
  import PageFoot from './PageFoot.svelte';
</script>

<section class="page bg-paper text-ink relative overflow-hidden">
  <PageHead title="07 · Toepassingen" />
  <div class="page__body">
    <div class="sec-head">
      <div>
        <h2 class="title-xl font-sans text-ink">Toepassingen.</h2>
        <p class="text-[12pt] leading-normal text-warm-800 mt-[6mm]">Waar het op uitkomt: site, slides, kaartje, signature. Dezelfde bouwstenen, andere ritmes.</p>
      </div>
    </div>

    <div class="apps">
      <!-- Site mock -->
      <div class="bg-surface border border-warm-400 rounded-sm overflow-hidden grid" style="grid-template-rows:1fr auto;">
        <div class="bg-paper relative overflow-hidden">
          <div class="mock-site bg-paper rounded-[3px] border border-warm-400">
            <div class="border-b border-warm-400 flex justify-between items-center px-[4mm]">
              <span class="font-sans font-semibold text-[8pt] tracking-[-0.03em] text-ink inline-flex items-baseline">
                arsene<span class="w-0.75 h-0.75 rounded-full bg-mint ml-px inline-block"></span>
              </span>
              <span class="font-mono text-[6pt] tracking-widest text-warm-600 flex gap-[4mm]">
                <span>WERK</span><span>OVER</span><span>CONTACT</span>
              </span>
            </div>
            <div class="p-[6mm_4mm] grid gap-[2mm]">
              <div class="font-mono text-[5.5pt] text-mint-deep tracking-widest uppercase">— Over</div>
              <div class="font-sans text-[16pt] leading-[0.98] tracking-[-0.04em] font-bold text-ink">Software op <em class="not-italic" style="background:linear-gradient(180deg,transparent 58%,#2ee5ac 58%,#2ee5ac 90%,transparent 90%);padding:0 1px;">jouw</em><br/>voorwaarden.</div>
              <div class="text-[6.5pt] text-warm-800 leading-[1.45]" style="max-width:38mm;">Voor MKB'ers die digitale infrastructuur willen bouwen die ze zélf kunnen beheren.</div>
              <div class="mt-[1mm] inline-flex items-center self-start bg-teal-deep text-teal-fg font-sans text-[6pt] font-semibold py-[2mm] px-[3mm] rounded-[1.5mm]">Begin een gesprek →</div>
            </div>
          </div>
        </div>
        <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
          <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Site · arsene.nl</div>
          <div class="font-mono text-[7.5pt] tracking-widest uppercase text-warm-600">Web · 1440 grid</div>
        </div>
      </div>

      <!-- Slide mock -->
      <div class="bg-surface border border-warm-400 rounded-sm overflow-hidden grid" style="grid-template-rows:1fr auto;">
        <div class="bg-paper relative overflow-hidden">
          <div class="mock-slide bg-teal-deep text-teal-fg rounded-[3px]">
            <div class="flex justify-between font-mono text-[6pt] tracking-[0.12em] uppercase text-[rgba(217,232,228,0.6)]">
              <span>— Project · KLM Cargo</span><span>03 / 12</span>
            </div>
            <div class="flex items-center">
              <div class="font-sans text-[19pt] leading-none tracking-[-0.04em] font-bold text-teal-fg">Eén dashboard.<br/><em class="not-italic text-mint-bright">Zes</em> minder Excels.</div>
            </div>
            <div class="flex justify-between items-baseline font-mono text-[6pt] tracking-widest uppercase text-[rgba(217,232,228,0.6)]">
              <span class="font-sans text-[7pt] text-teal-fg font-semibold tracking-[-0.03em] not-uppercase inline-flex items-baseline">
                arsene<span class="w-[2.5px] h-[2.5px] rounded-full bg-mint ml-px inline-block"></span>
              </span>
              <span>2026</span>
            </div>
          </div>
        </div>
        <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
          <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Slides · 16:9</div>
          <div class="font-mono text-[7.5pt] tracking-widest uppercase text-warm-600">PPTX · keynote</div>
        </div>
      </div>

      <!-- Business card mock -->
      <div class="bg-surface border border-warm-400 rounded-sm overflow-hidden grid" style="grid-template-rows:1fr auto;">
        <div class="relative overflow-hidden">
          <div class="mock-card" style="background:repeating-linear-gradient(0deg,rgba(0,0,0,0.025) 0 1px,transparent 1px 6mm),repeating-linear-gradient(90deg,rgba(0,0,0,0.025) 0 1px,transparent 1px 6mm),#f4f1e8;">
            <div class="card bg-paper border border-warm-400 rounded-[1.5mm]" style="box-shadow:0 1mm 3mm rgba(0,0,0,0.06);">
              <div class="flex justify-between items-baseline">
                <span class="font-sans font-semibold text-[11pt] tracking-[-0.04em] text-ink inline-flex items-baseline">
                  arsene<span class="w-1 h-1 rounded-full bg-mint ml-[1.5px] inline-block" style="box-shadow:0 0 6px #00b585;"></span>
                </span>
                <span class="font-mono text-[5pt] tracking-[0.12em] uppercase text-warm-600">Arsene</span>
              </div>
              <div class="self-end">
                <div class="font-sans text-[8pt] font-semibold tracking-[-0.01em] text-ink">Julian van der Horst</div>
                <div class="font-mono text-[6pt] tracking-[0.08em] uppercase text-warm-600 mt-[0.5mm]">Founder · Engineer</div>
              </div>
              <div class="font-mono text-[5.5pt] tracking-[0.06em] text-warm-800 flex justify-between">
                <span>+31 6 12 34 56 78</span><span>arsene.nl</span>
              </div>
            </div>
          </div>
        </div>
        <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
          <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Visitekaart · 85×55</div>
          <div class="font-mono text-[7.5pt] tracking-widest uppercase text-warm-600">Print · uncoated 350g</div>
        </div>
      </div>

      <!-- Email signature mock -->
      <div class="bg-surface border border-warm-400 rounded-sm overflow-hidden grid" style="grid-template-rows:1fr auto;">
        <div class="relative overflow-hidden bg-white">
          <div class="mock-sig">
            <div class="sig font-sans text-[8pt] leading-[1.4] text-ink">
              <div class="sq bg-teal-deep text-teal-fg font-sans font-semibold text-[10mm] leading-none tracking-tighter">
                <span class="glyph">a<span class="pin"></span></span>
              </div>
              <div class="who">
                <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Julian van der Horst</div>
                <div class="text-[8pt] text-warm-600 mt-[0.5mm]">Arsene · Founder</div>
                <div class="mt-[2mm] font-mono text-[7pt] text-mint-deep tracking-[0.04em]">arsene.nl · +31 6 12 34 56 78</div>
              </div>
            </div>
          </div>
        </div>
        <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
          <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">E-mail signature</div>
          <div class="font-mono text-[7.5pt] tracking-widest uppercase text-warm-600">Mail · HTML/plain</div>
        </div>
      </div>
    </div>
  </div>
  <PageFoot page="09 / 11" />
</section>
