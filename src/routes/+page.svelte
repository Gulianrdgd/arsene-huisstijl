<div class="book bg-[#d8d3c2]">

  <!-- ============================================================
       PAGE 1 — COVER
       ============================================================ -->
  <section class="page cover bg-paper text-ink relative overflow-hidden">
    <div class="top flex justify-between items-center">
      <div class="brand inline-flex items-baseline font-sans tracking-[-0.04em] font-semibold text-[18pt] text-ink">
        arsene<span class="w-2 h-2 rounded-full bg-mint ml-1 inline-block" style="box-shadow:0 0 14px #00b585;"></span>
      </div>
    </div>

    <div class="center">
      <h1 class="font-sans text-ink">arsene<br/>huis<span class="accent">stijl</span>.</h1>
      <div class="lede mt-[8mm] max-w-1/2">
        <p class="text-[11pt] leading-[1.5] text-warm-800">Een werkboek over hoe we eruit zien, hoe we klinken, en vooral hoe we dat consistent houden zonder er verkrampt over te doen.</p>
      </div>
    </div>

    <div class="bottom flex justify-between items-end font-mono text-[8.5pt] tracking-[0.1em] uppercase text-warm-600">
      <div>Arsene</div>
      <div>28 mei 2026</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 2 — INTRO + INHOUD
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>Inleiding · Inhoud</div>
    </div>
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
            {#each [
              ['01','Woordmerk','03'],
              ['02','Beeldmerk & clearspace','04'],
              ['03','Kleur','05'],
              ['04','Typografie','06'],
              ['05','Toon & taal','07'],
              ['06','Detailtaal','08'],
              ['07','Toepassingen','09'],
              ['08','Taglines','10'],
            ] as [n, title, p] (n)}
              <li class="border-b border-warm-400 text-[11pt] py-[2mm]">
                <span class="font-mono text-[9pt] text-warm-600 tracking-[0.06em]">{n}</span>
                <strong class="font-medium tracking-[-0.01em]">{title}</strong>
                <span class="font-mono text-[9pt] text-warm-600">{p}</span>
              </li>
            {/each}
          </ol>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>02 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 3 — 01 WOORDMERK
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>01 · Woordmerk</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Woordmerk.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Eén woord, kleine letters, een muntgroene punt. Het hele merk komt samen in dit teken: de naam zonder kapsones, en die ene <span class="mark">pin</span> als signaal dat we nog leven.</p>
        </div>
      </div>

      <div class="logo-hero bg-teal-deep text-teal-fg rounded-[4px] relative grid place-items-center mb-[8mm]">
        <div class="corner font-mono text-[8pt] tracking-[0.1em] text-[rgba(217,232,228,0.55)] uppercase">Primair · op Teal Deep</div>
        <span class="wordmark wordmark--xxl font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-teal-fg">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
      </div>

      <div class="anatomy mb-[6mm]">
        {#each [
          ['Letterbeeld','Geist 600, lowercase'],
          ['Tracking','−4% (−0.04em)'],
          ['Pin','¼ van x-hoogte, Mint #00B585'],
          ['Pin-offset','6 px links, baseline-aligned'],
        ] as [k, v] (k)}
          <div class="border-t border-warm-400 pt-[3mm]">
            <div class="font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600 mb-[1mm]">{k}</div>
            <div class="text-[10pt] leading-[1.4] text-ink">{v}</div>
          </div>
        {/each}
      </div>

      <div class="h-px bg-warm-400 mb-[6mm]"></div>

      <div class="grid gap-[6mm] items-end" style="grid-template-columns:1fr 1fr 1fr;">
        {#each [
          ['wordmark--lg','— Groot','Site-hero, cover, banner. Pin met glow.'],
          ['wordmark--md','— Medium','Navigatie, slide-footer, signature.'],
          ['wordmark--sm','— Klein','Visitekaart, footnotes. Pin zonder glow.'],
        ] as [cls, label, note] (cls)}
          <div>
            <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[4mm]">{label}</div>
            <span class="wordmark {cls} font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
            <div class="text-[8.5pt] leading-[1.5] text-warm-600 mt-[3mm]">{note}</div>
          </div>
        {/each}
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>03 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 4 — 02 BEELDMERK & CLEARSPACE
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>02 · Beeldmerk &amp; clearspace</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Beeldmerk &amp; clearspace.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Voor favicons, avatars en alles wat te klein is voor de woordmerk: het teal-vierkant met de pin in het midden. Halo-ring komt mee, of niet — afhankelijk van de plek.</p>
        </div>
      </div>

      <div class="grid gap-[6mm] mb-[6mm]" style="grid-template-columns:1fr 1fr;">
        <!-- Do: clearspace -->
        <div class="swatch-card border border-warm-400 rounded-[4px] bg-surface">
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
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center text-center">Doe dit</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Houd minstens één pin-breedte clearspace aan alle zijden.</span>
          </div>
        </div>

        <!-- Do: proportional scaling -->
        <div class="swatch-card border border-warm-400 rounded-[4px] bg-surface">
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
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center">Doe dit</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Schaal proportioneel. De pin blijft ¼ van het vierkant.</span>
          </div>
        </div>
      </div>

      <div class="dodont">
        <!-- Niet doen: stretchen -->
        <div class="swatch-card swatch-card--sm border border-warm-400 rounded-[4px] bg-surface">
          <div class="demo bg-paper grid place-items-center">
            <span class="stretched">arsene<span class="pin"></span></span>
          </div>
          <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Nooit horizontaal of verticaal stretchen.</span>
          </div>
        </div>
        <!-- Niet doen: verkeerde kleur pin -->
        <div class="swatch-card swatch-card--sm border border-warm-400 rounded-[4px] bg-surface">
          <div class="demo bg-paper grid place-items-center">
            <span class="wrong-color">arsene<span class="pin"></span></span>
          </div>
          <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Geen andere kleur voor de pin. Mint blijft mint.</span>
          </div>
        </div>
        <!-- Niet doen: drukke achtergrond -->
        <div class="swatch-card swatch-card--sm border border-warm-400 rounded-[4px] bg-surface">
          <div class="demo grid place-items-center" style="background: repeating-linear-gradient(45deg, rgba(0,0,0,0.06) 0 2px, transparent 2px 8px), #f4f1e8;">
            <span class="wordmark wordmark--lg font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink">arsene<span class="pin inline-block rounded-full bg-mint"></span></span>
          </div>
          <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Niet op drukke achtergronden. Houd het rustig.</span>
          </div>
        </div>
        <!-- Niet doen: kapitalen -->
        <div class="swatch-card swatch-card--sm border border-warm-400 rounded-[4px] bg-surface">
          <div class="demo bg-paper grid place-items-center">
            <span class="wordmark wordmark--lg font-sans font-semibold tracking-[-0.04em] leading-none inline-flex items-baseline text-ink uppercase">ARSENE<span class="pin inline-block rounded-full bg-mint"></span></span>
          </div>
          <div class="flex items-center gap-[3mm] p-[4mm_5mm] border-t border-warm-400">
            <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-signal text-white text-center">Niet doen</span>
            <span class="text-[9.5pt] leading-[1.35] text-warm-800">Nooit kapitalen. Het merk is consequent lowercase.</span>
          </div>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>04 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 5 — 03 KLEUR
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>03 · Kleur</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Kleur.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Warm papier als basis, diepteal voor gewicht, mint als signaal. Drie families — meer is bijna nooit nodig.</p>
        </div>
      </div>

      {#each [
        {
          label: '— Anker · papier & inkt',
          swatches: [
            { bg: '#f4f1e8', name: 'Paper',    hex: '#F4F1E8', rgb: '244 · 241 · 232', role: 'Pagina-achtergrond. Warm crème.', border: true },
            { bg: '#ebe7d8', name: 'Warm 200', hex: '#EBE7D8', rgb: '235 · 231 · 216', role: 'Wisselsecties, hover.', border: true },
            { bg: '#d8d3c2', name: 'Warm 400', hex: '#D8D3C2', rgb: '216 · 211 · 194', role: 'Randen, dividers.', border: true },
            { bg: '#14120f', name: 'Ink',      hex: '#14120F', rgb: '20 · 18 · 15',    role: 'Tekst. Headlines.', border: false },
          ]
        },
        {
          label: '— Diepte · teal',
          swatches: [
            { bg: '#06120f', name: 'Teal Deep', hex: '#06120F', rgb: '6 · 18 · 15',   role: 'Donkere ankers, knoppen, slides.', border: false },
            { bg: '#0a1a17', name: 'Teal Card', hex: '#0A1A17', rgb: '10 · 26 · 23',  role: 'Donkere kaarten, panels.', border: false },
            { bg: '#4d4a41', name: 'Warm 800',  hex: '#4D4A41', rgb: '77 · 74 · 65',  role: 'Secundaire tekst.', border: false },
            { bg: '#918c7e', name: 'Warm 600',  hex: '#918C7E', rgb: '145 · 140 · 126',role: 'Metadata, mono-labels.', border: false },
          ]
        },
        {
          label: '— Signaal · mint & rood',
          swatches: [
            { bg: '#00b585', name: 'Mint',       hex: '#00B585', rgb: '0 · 181 · 133', role: 'Primair accent. De pin.', border: false },
            { bg: '#2ee5ac', name: 'Mint Bright',hex: '#2EE5AC', rgb: '46 · 229 · 172',role: 'Marker, highlight-blokken.', border: false },
            { bg: '#007f5f', name: 'Mint Deep',  hex: '#007F5F', rgb: '0 · 127 · 95',  role: 'Eyebrows, pressed states.', border: false },
            { bg: '#d83a20', name: 'Signal',     hex: '#D83A20', rgb: '216 · 58 · 32', role: 'Errors, waarschuwingen. Spaarzaam.', border: false },
          ]
        },
      ] as row (row.label)}
        <div class="mb-[6mm]">
          <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600 mb-[3mm]">{row.label}</div>
          <div class="palette">
            {#each row.swatches as s (s.name)}
              <div class="swatch rounded-[4px] overflow-hidden border border-warm-400 bg-surface">
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

      <div class="text-[8.5pt] leading-[1.5] text-warm-600 mt-[4mm]">
        Paper draagt het beeld; teal en mint zijn accent. Mint mag op paper en op teal; op mint zelf alleen teal-tekst. Geen gradients, geen pasteltinten buiten dit palet.
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>05 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 6 — 04 TYPOGRAFIE
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>04 · Typografie</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Typografie.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Geist voor het werk, Geist Mono voor de bijschriften. Twee families, één toon: helder, mechanisch, modern.</p>
        </div>
      </div>

      <div class="type-pair mb-[4mm]">
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm]">
          <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-mint-deep mb-[1mm]">— Primair</div>
          <div class="text-[16pt] font-semibold tracking-[-0.02em] mb-[4mm] text-ink">Geist</div>
          <div class="text-[28pt] tracking-[-0.02em] leading-none mb-[2mm] text-ink">AaBb 0123</div>
          <div class="text-[9pt] text-warm-800 mb-[3mm] tracking-[0.02em]">abcdefghijklmnopqrstuvwxyz</div>
          <div class="text-[8.5pt] leading-[1.5] text-warm-600">Alle gewichten 300–900. Sans-serif met scherpe terminals. Voor headlines, body, UI.</div>
        </div>
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm]">
          <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-mint-deep mb-[1mm]">— Detail</div>
          <div class="font-mono text-[16pt] font-semibold tracking-[-0.02em] mb-[4mm] text-ink">Geist Mono</div>
          <div class="font-mono text-[28pt] leading-none mb-[2mm] font-medium text-ink">AaBb 0123</div>
          <div class="font-mono text-[9pt] text-warm-800 mb-[3mm]">abcdef · 12345 · ··-→</div>
          <div class="text-[8.5pt] leading-[1.5] text-warm-600">Gewichten 400/500/600. Voor eyebrows, metadata, codetekst, sectienummers.</div>
        </div>
      </div>

      <div class="h-px bg-warm-400 my-[6mm]"></div>

      <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[5mm]">— Schaal</div>
      <div class="flex flex-col gap-[4mm]">
        {#each [
          { label: 'Display 2XL', style: 'font-size:32pt;line-height:0.98;letter-spacing:-0.05em;font-weight:700;', text: 'arsene huisstijl.', meta: '84 / 0.95 · 700' },
          { label: 'Display XL',  style: 'font-size:24pt;line-height:1;letter-spacing:-0.045em;font-weight:700;',  text: 'Software op jouw voorwaarden.', meta: '64 / 1.0 · 700' },
          { label: 'Heading 1',   style: 'font-size:18pt;line-height:1.05;letter-spacing:-0.035em;font-weight:700;',text: 'Een sectie met gewicht.', meta: '44 / 1.05 · 700' },
          { label: 'Heading 2',   style: 'font-size:14pt;line-height:1.15;letter-spacing:-0.02em;font-weight:600;', text: 'Een subsectie binnen de pagina.', meta: '32 / 1.15 · 600' },
          { label: 'Lede',        style: 'font-size:11pt;line-height:1.5;color:#4d4a41;font-weight:400;',           text: 'Een grotere alinea die als opmaat naar een sectie dient — iets meer adem, iets minder druk dan de body.', meta: '20 / 1.5 · 400' },
          { label: 'Body',        style: 'font-size:10pt;line-height:1.55;color:#4d4a41;font-weight:400;',          text: 'De gewone tekst die de meeste pagina\'s draagt. Gebruik Warm 800 op papier; volle Ink wordt te zwaar.', meta: '16 / 1.55 · 400' },
        ] as row (row.label)}
          <div class="type-row border-t border-warm-400 pt-[3mm]">
            <div class="font-mono text-[8.5pt] tracking-[0.1em] uppercase text-warm-600">{row.label}</div>
            <div class="font-sans text-ink" style={row.style}>{row.text}</div>
            <div class="font-mono text-[8pt] text-warm-600 text-right">{row.meta}</div>
          </div>
        {/each}
        <div class="type-row border-t border-warm-400 pt-[3mm]">
          <div class="font-mono text-[8.5pt] tracking-[0.1em] uppercase text-warm-600">Mono · Eyebrow</div>
          <div class="font-mono text-mint-deep" style="font-size:9pt;letter-spacing:0.14em;text-transform:uppercase;font-weight:500;">— Sectielabel boven een titel</div>
          <div class="font-mono text-[8pt] text-warm-600 text-right">11 / 1.4 · 500 · +0.14em</div>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>06 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 7 — 05 TOON & TAAL
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>05 · Toon &amp; taal</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Toon &amp; taal.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">We schrijven zoals we praten — droog, concreet, een tikje Nederlands. We schoppen niet, maar we vermijden ook het lege galmen van het consultancy-vocabulaire.</p>
        </div>
      </div>

      <div class="grid gap-[6mm] mb-[8mm]" style="grid-template-columns:1fr 1fr 1fr;">
        {#each [
          ['— Persoon', 'Tweede persoon: jij, jouw, we, ons. Spreek direct, niet via een omweg.'],
          ['— Hoofdletters', 'Sentence case. Titels niet als Title Case. Eyebrows in uppercase, alléén in mono.'],
          ['— Emoji', 'Nee. Het merk is niet emoji-gedreven. In interne Slack mag het, in product en site niet.'],
        ] as [label, text] (label)}
          <div>
            <div class="font-mono text-[8pt] tracking-[0.14em] uppercase font-medium text-mint-deep mb-[2mm]">{label}</div>
            <div class="text-[8.5pt] leading-[1.5] text-warm-600">{text}</div>
          </div>
        {/each}
      </div>

      <div class="flex flex-col gap-[0]">
        {#each [
          { do: true, nl: '"We bouwen \'m zo dat je hem morgen aan je buurjongen kan geven en die er ook wat van bakt."', en: 'EN — We build it so you could hand it to the neighbour\'s kid tomorrow and they\'d still ship.' },
          { do: false, nl: '"Onze proprietary cloud-native AI-stack democratiseert digitale transformatie voor het MKB."', en: 'EN — Our proprietary cloud-native AI stack democratises digital transformation for SMBs.' },
          { do: true, nl: '"WordPress, met een visuele editor. Saai? Misschien. Maar over vijf jaar werkt het nog steeds — en iedere developer kan eraan sleutelen."', en: 'EN — WordPress, with a visual editor. Boring? Maybe. But it\'ll still work in five years, and any developer can pick it up.' },
          { do: false, nl: '"Onze AI-gedreven oplossing transformeert uw bedrijfsprocessen middels next-gen synergie."', en: 'EN — Our AI-driven solution transforms your business through next-gen synergy.' },
          { do: true, nl: '"We verkopen geen ChatGPT-licenties. We kijken eerst waar AI in jouw bedrijf écht iets oplost — en waar het in de weg zit."', en: 'EN — We don\'t resell ChatGPT licences. We figure out where AI actually solves something — and where it gets in the way.' },
        ] as item (item.nl)}
          <div class="voice-item border-t border-warm-400 py-[4mm] {item.do ? '' : 'voice-dont'}">
            <div>
              {#if item.do}
                <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center bg-mint text-white text-center">Doe dit</span>
              {:else}
                <span class="font-mono text-[8pt] leading-none tracking-[0.1em] uppercase py-[1.6mm] px-[3mm] rounded-full inline-flex items-center border border-signal text-signal text-center">Niet doen</span>
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
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>07 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 8 — 06 DETAILTAAL
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>06 · Detailtaal</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Detailtaal.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Kleine terugkerende elementen die het beeld dragen: de marker, de pin, het eyebrow-label, de sectienummers. Gebruik ze met mate, niet als sticker-album.</p>
        </div>
      </div>

      <div class="detail-grid">
        <!-- Marker -->
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Marker</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600">accent · mint bright</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
            <div class="font-sans text-[18pt] font-bold tracking-[-0.03em] text-ink">Software op <span class="mark">jouw voorwaarden</span>.</div>
          </div>
          <div class="text-[9pt] leading-[1.45] text-warm-800">Een hoogtepunt op één of twee woorden per blok. Nooit op een hele zin. Bandhoogte ≈ 36% van de regelhoogte, onderaan uitgelijnd.</div>
        </div>

        <!-- De pin -->
        <div class="bg-teal-deep border-teal-deep rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-teal-fg">De pin</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-[rgba(217,232,228,0.55)]">mint · ≥ 6 px</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center rounded-[3px] bg-[rgba(255,255,255,0.04)]">
            <div class="inline-flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-mint inline-block" style="box-shadow:0 0 14px #00b585;"></span>
              <span class="font-mono text-[10pt] tracking-[0.06em] text-teal-fg">live · uptime 99.98%</span>
            </div>
          </div>
          <div class="text-[9pt] leading-[1.45] text-[rgba(217,232,228,0.7)]">Het signaal "we leven". Gebruik in statusrijtjes, on-states, en als losse interpunctie tussen mono-labels. Glow alleen op donker.</div>
        </div>

        <!-- Eyebrow-label -->
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Eyebrow-label</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600">mono · 0.14em · upper</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
            <div class="font-mono text-[10pt] tracking-[0.16em] uppercase text-mint-deep font-medium">— 03 · Kleur</div>
          </div>
          <div class="text-[9pt] leading-[1.45] text-warm-800">Mono, uppercase, met em-dash ervoor of het sectienummer. Altijd Mint Deep op paper, Mint Bright op teal.</div>
        </div>

        <!-- Sectienummers -->
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Sectienummers</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600">mono · 2-digit</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
            <div class="font-mono text-[9pt] tracking-[0.08em] text-warm-600 inline-flex items-baseline gap-[8mm]">
              <span>01</span><span>02</span><span class="text-ink">— 03</span><span>04</span><span>05</span>
            </div>
          </div>
          <div class="text-[9pt] leading-[1.45] text-warm-800">Altijd twee cijfers. Niet 1 maar 01. Op een lijn, gescheiden door witruimte. De huidige sectie krijgt een em-dash ervoor.</div>
        </div>

        <!-- Knop -->
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Knop</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600">teal deep · 6px radius</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
            <span class="inline-flex items-center gap-2 px-4 py-[9px] rounded-[4px] font-sans font-semibold text-[11pt] bg-teal-deep text-teal-fg">Begin een gesprek →</span>
          </div>
          <div class="text-[9pt] leading-[1.45] text-warm-800">Strak, bijna haakse hoeken (6 px). Geen schaduw, geen gradient. Hover: ink. Outline-variant: 1.5 px boord, ink-kleur.</div>
        </div>

        <!-- Em-dash -->
        <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm] grid gap-[4mm]">
          <div class="flex justify-between items-baseline">
            <div class="font-sans text-[13pt] font-semibold tracking-[-0.01em] text-ink">Em-dash</div>
            <div class="font-mono text-[8pt] tracking-[0.1em] uppercase text-warm-600">— · niet -</div>
          </div>
          <div class="min-h-[20mm] grid place-items-center bg-paper rounded-[3px]">
            <div class="text-[16pt] font-medium tracking-[-0.01em] text-ink">Klein bedrijf — echte infrastructuur.</div>
          </div>
          <div class="text-[9pt] leading-[1.45] text-warm-800">Het em-dash (—) is het Arsene-leesteken bij uitstek. Spatie ervoor en erna. Geen hyphens, geen ndashen voor losse pauzes.</div>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>08 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 9 — 07 TOEPASSINGEN
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>07 · Toepassingen</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Toepassingen.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Waar het op uitkomt: site, slides, kaartje, signature. Dezelfde bouwstenen, andere ritmes.</p>
        </div>
      </div>

      <div class="apps">
        <!-- Site mock -->
        <div class="bg-surface border border-warm-400 rounded-[4px] overflow-hidden grid" style="grid-template-rows:1fr auto;">
          <div class="bg-paper relative overflow-hidden">
            <div class="mock-site bg-paper rounded-[3px] border border-warm-400">
              <div class="border-b border-warm-400 flex justify-between items-center px-[4mm]">
                <span class="font-sans font-semibold text-[8pt] tracking-[-0.03em] text-ink inline-flex items-baseline">
                  arsene<span class="w-[3px] h-[3px] rounded-full bg-mint ml-[1px] inline-block"></span>
                </span>
                <span class="font-mono text-[6pt] tracking-[0.1em] text-warm-600 flex gap-[4mm]">
                  <span>WERK</span><span>OVER</span><span>CONTACT</span>
                </span>
              </div>
              <div class="p-[6mm_4mm] grid gap-[2mm]">
                <div class="font-mono text-[5.5pt] text-mint-deep tracking-[0.1em] uppercase">— Over</div>
                <div class="font-sans text-[16pt] leading-[0.98] tracking-[-0.04em] font-bold text-ink">Software op <em class="not-italic" style="background:linear-gradient(180deg,transparent 58%,#2ee5ac 58%,#2ee5ac 90%,transparent 90%);padding:0 1px;">jouw</em><br/>voorwaarden.</div>
                <div class="text-[6.5pt] text-warm-800 leading-[1.45]" style="max-width:38mm;">Voor MKB'ers die digitale infrastructuur willen bouwen die ze zélf kunnen beheren.</div>
                <div class="mt-[1mm] inline-flex items-center self-start bg-teal-deep text-teal-fg font-sans text-[6pt] font-semibold py-[2mm] px-[3mm] rounded-[1.5mm]">Begin een gesprek →</div>
              </div>
            </div>
          </div>
          <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
            <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Site · arsene.nl</div>
            <div class="font-mono text-[7.5pt] tracking-[0.1em] uppercase text-warm-600">Web · 1440 grid</div>
          </div>
        </div>

        <!-- Slide mock -->
        <div class="bg-surface border border-warm-400 rounded-[4px] overflow-hidden grid" style="grid-template-rows:1fr auto;">
          <div class="bg-paper relative overflow-hidden">
            <div class="mock-slide bg-teal-deep text-teal-fg rounded-[3px]">
              <div class="flex justify-between font-mono text-[6pt] tracking-[0.12em] uppercase text-[rgba(217,232,228,0.6)]">
                <span>— Project · KLM Cargo</span><span>03 / 12</span>
              </div>
              <div class="flex items-center">
                <div class="font-sans text-[19pt] leading-none tracking-[-0.04em] font-bold text-teal-fg">Eén dashboard.<br/><em class="not-italic text-mint-bright">Zes</em> minder Excels.</div>
              </div>
              <div class="flex justify-between items-baseline font-mono text-[6pt] tracking-[0.1em] uppercase text-[rgba(217,232,228,0.6)]">
                <span class="font-sans text-[7pt] text-teal-fg font-semibold tracking-[-0.03em] not-uppercase inline-flex items-baseline">
                  arsene<span class="w-[2.5px] h-[2.5px] rounded-full bg-mint ml-[1px] inline-block"></span>
                </span>
                <span>2026</span>
              </div>
            </div>
          </div>
          <div class="p-[4mm_5mm] border-t border-warm-400 flex justify-between items-baseline">
            <div class="font-sans text-[11pt] font-semibold tracking-[-0.01em] text-ink">Slides · 16:9</div>
            <div class="font-mono text-[7.5pt] tracking-[0.1em] uppercase text-warm-600">PPTX · keynote</div>
          </div>
        </div>

        <!-- Business card mock -->
        <div class="bg-surface border border-warm-400 rounded-[4px] overflow-hidden grid" style="grid-template-rows:1fr auto;">
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
            <div class="font-mono text-[7.5pt] tracking-[0.1em] uppercase text-warm-600">Print · uncoated 350g</div>
          </div>
        </div>

        <!-- Email signature mock -->
        <div class="bg-surface border border-warm-400 rounded-[4px] overflow-hidden grid" style="grid-template-rows:1fr auto;">
          <div class="relative overflow-hidden bg-white">
            <div class="mock-sig">
              <div class="sig font-sans text-[8pt] leading-[1.4] text-ink">
                <div class="sq bg-teal-deep text-teal-fg font-sans font-semibold text-[10mm] leading-none tracking-[-0.05em]">
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
            <div class="font-mono text-[7.5pt] tracking-[0.1em] uppercase text-warm-600">Mail · HTML/plain</div>
          </div>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>09 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 10 — 08 TAGLINES
       ============================================================ -->
  <section class="page bg-paper text-ink relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-ink">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>08 · Taglines</div>
    </div>
    <div class="page__body">
      <div class="sec-head">
        <div>
          <h2 class="title-xl font-sans text-ink">Taglines.</h2>
          <p class="text-[12pt] leading-[1.5] text-warm-800 mt-[6mm]">Eén regel, één boodschap. Hieronder een set die we afhankelijk van de context kunnen inzetten. Niet hagelen — kies bewust.</p>
        </div>
      </div>

      <div class="tag-grid">
        {#each [
          { nl: 'Alles kan.', en: 'EN — Anything\'s possible.', note: 'Open, optimistisch, heel Nederlands. Voorkeur voor home-hero.' },
          { nl: 'Jij de sleutels.\nWij het zware werk.', en: 'EN — You keep the keys. We do the heavy lifting.', note: 'Meest letterlijk aan de positionering. Voor uitleg-context.' },
          { nl: 'Software op jouw voorwaarden.', en: 'EN — Software on your terms.', note: 'Helder. Maakt het no-lock-in-statement.' },
          { nl: 'Bouw mee, beheer zelf.', en: 'EN — Build along. Run it yourself.', note: 'Actief, samenwerkend. Voor case-pages en aanbiedingen.' },
          { nl: 'Klein bedrijf,\nechte infrastructuur.', en: 'EN — Small business. Real infrastructure.', note: 'Tegen het "speelgoed-software"-stigma in MKB.' },
          { nl: 'Geen lock-in.\nGeen onzin.', en: 'EN — No lock-in. No nonsense.', note: 'Punchy, een tikkeltje brutaal. Voor sales-context.' },
        ] as card (card.nl)}
          <div class="bg-surface border border-warm-400 rounded-[4px] p-[6mm]">
            <div class="text-[26pt] leading-none tracking-[-0.045em] font-bold text-ink mb-[3mm]" style="white-space:pre-line;">{card.nl}</div>
            <div class="text-[11pt] italic tracking-[-0.01em] text-warm-800 mb-[3mm]">{card.en}</div>
            <div class="font-mono text-[8pt] tracking-[0.06em] text-warm-600 border-t border-warm-400 pt-[3mm]">{card.note}</div>
          </div>
        {/each}
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-warm-600">
      <div>Arsene Huisstijl</div>
      <div>10 / 11</div>
    </div>
  </section>

  <!-- ============================================================
       PAGE 11 — COLOFON
       ============================================================ -->
  <section class="page page--teal bg-teal-deep text-teal-fg relative overflow-hidden">
    <div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-[rgba(217,232,228,0.55)]">
      <div class="inline-flex items-baseline gap-[4px] font-sans tracking-[-0.03em] font-semibold text-[10pt] text-teal-fg">
        arsene<span class="w-[6px] h-[6px] rounded-full bg-mint ml-[1px] inline-block -translate-y-[0.5px]"></span>
      </div>
      <div>+ · Colofon</div>
    </div>
    <div class="page__body">
      <div class="colophon">
        <div class="head-block">
          <div>
            <div class="font-mono text-[8.5pt] tracking-[0.14em] uppercase font-medium text-mint-bright mb-[6mm]">— Colofon</div>
            <h2 class="title-xl font-sans text-teal-fg">Tot zover.</h2>
            <p class="text-[12pt] leading-[1.5] text-teal-fg opacity-[0.78] mt-[6mm]">Vragen, dubbelpunten, of een uiting die niet past in dit boekje? Stuur het op. We werken liever met je mee dan er omheen.</p>
          </div>
          <div class="brand-mark brand-mark--soft flex-shrink-0" style="width:28mm;font-size:20mm;border-radius:5mm;">
            <span class="glyph">a<span class="pin"></span></span>
          </div>
        </div>

        <div class="w-full text-[10pt] leading-[1.5]">
          {#each [
            ['Document', 'Arsene Huisstijlhandleiding'],
            ['Datum', '28 mei 2026'],
            ['Onderhoud', 'Arsene · brand@arsene.nl'],
            ['Vragen', 'info@arsene.nl'],
            ['Typografie', 'Geist & Geist Mono'],
          ] as [k, v] (k)}
            <div class="colophon meta-row border-t py-[3mm]" style="border-color:rgba(217,232,228,0.18);">
              <div class="font-mono text-[8.5pt] tracking-[0.1em] uppercase text-[rgba(217,232,228,0.55)]">{k}</div>
              <div class="text-teal-fg">{v}</div>
            </div>
          {/each}
        </div>

        <div class="closing font-sans text-teal-fg">
          alles<br/>kan<span class="closing-pin"></span>
        </div>
      </div>
    </div>
    <div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase text-[rgba(217,232,228,0.55)]">
      <div>Arsene Huisstijl</div>
      <div>11 / 11</div>
    </div>
  </section>

</div>
