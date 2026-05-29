export const tocItems = [
  { n: '01', title: 'Woordmerk',              page: '03' },
  { n: '02', title: 'Beeldmerk & clearspace', page: '04' },
  { n: '03', title: 'Kleur',                  page: '05' },
  { n: '04', title: 'Typografie',             page: '06' },
  { n: '05', title: 'Toon & taal',            page: '07' },
  { n: '06', title: 'Detailtaal',             page: '08' },
  { n: '07', title: 'Toepassingen',           page: '09' },
  { n: '08', title: 'Taglines',               page: '10' },
];

export const anatomyItems: [string, string][] = [
  ['Letterbeeld', 'Geist 600, lowercase'],
  ['Tracking',    '−4% (−0.04em)'],
  ['Pin',         '¼ van x-hoogte, Mint #00B585'],
  ['Pin-offset',  '6 px links, baseline-aligned'],
];

export const wordmarkSizes = [
  { cls: 'wordmark--lg', label: '— Groot',  note: 'Site-hero, cover, banner. Pin met glow.' },
  { cls: 'wordmark--md', label: '— Medium', note: 'Navigatie, slide-footer, signature.' },
  { cls: 'wordmark--sm', label: '— Klein',  note: 'Visitekaart, footnotes. Pin zonder glow.' },
];

export const colorGroups = [
  {
    label: '— Anker · papier & inkt',
    swatches: [
      { bg: '#f4f1e8', name: 'Paper',     hex: '#F4F1E8', rgb: '244 · 241 · 232', role: 'Pagina-achtergrond. Warm crème.',  border: true  },
      { bg: '#ebe7d8', name: 'Warm 200',  hex: '#EBE7D8', rgb: '235 · 231 · 216', role: 'Wisselsecties, hover.',             border: true  },
      { bg: '#d8d3c2', name: 'Warm 400',  hex: '#D8D3C2', rgb: '216 · 211 · 194', role: 'Randen, dividers.',                 border: true  },
      { bg: '#14120f', name: 'Ink',       hex: '#14120F', rgb: '20 · 18 · 15',    role: 'Tekst. Headlines.',                 border: false },
    ],
  },
  {
    label: '— Diepte · teal',
    swatches: [
      { bg: '#06120f', name: 'Teal Deep', hex: '#06120F', rgb: '6 · 18 · 15',     role: 'Donkere ankers, knoppen, slides.', border: false },
      { bg: '#0a1a17', name: 'Teal Card', hex: '#0A1A17', rgb: '10 · 26 · 23',    role: 'Donkere kaarten, panels.',          border: false },
      { bg: '#4d4a41', name: 'Warm 800',  hex: '#4D4A41', rgb: '77 · 74 · 65',    role: 'Secundaire tekst.',                 border: false },
      { bg: '#918c7e', name: 'Warm 600',  hex: '#918C7E', rgb: '145 · 140 · 126', role: 'Metadata, mono-labels.',            border: false },
    ],
  },
  {
    label: '— Signaal · mint & rood',
    swatches: [
      { bg: '#00b585', name: 'Mint',        hex: '#00B585', rgb: '0 · 181 · 133',  role: 'Primair accent. De pin.',            border: false },
      { bg: '#2ee5ac', name: 'Mint Bright', hex: '#2EE5AC', rgb: '46 · 229 · 172', role: 'Marker, highlight-blokken.',         border: false },
      { bg: '#007f5f', name: 'Mint Deep',   hex: '#007F5F', rgb: '0 · 127 · 95',   role: 'Eyebrows, pressed states.',          border: false },
      { bg: '#d83a20', name: 'Signal',      hex: '#D83A20', rgb: '216 · 58 · 32',  role: 'Errors, waarschuwingen. Spaarzaam.', border: false },
    ],
  },
];

export const typeScale = [
  { label: 'Display 2XL', style: 'font-size:32pt;line-height:0.98;letter-spacing:-0.05em;font-weight:700;',  text: 'arsene huisstijl.',               meta: '84 / 0.95 · 700' },
  { label: 'Display XL',  style: 'font-size:24pt;line-height:1;letter-spacing:-0.045em;font-weight:700;',    text: 'Software op jouw voorwaarden.',   meta: '64 / 1.0 · 700'  },
  { label: 'Heading 1',   style: 'font-size:18pt;line-height:1.05;letter-spacing:-0.035em;font-weight:700;', text: 'Een sectie met gewicht.',         meta: '44 / 1.05 · 700' },
  { label: 'Heading 2',   style: 'font-size:14pt;line-height:1.15;letter-spacing:-0.02em;font-weight:600;',  text: 'Een subsectie binnen de pagina.', meta: '32 / 1.15 · 600' },
  { label: 'Lede',        style: 'font-size:11pt;line-height:1.5;color:#4d4a41;font-weight:400;',            text: 'Een grotere alinea die als opmaat naar een sectie dient — iets meer adem, iets minder druk dan de body.', meta: '20 / 1.5 · 400' },
  { label: 'Body',        style: 'font-size:10pt;line-height:1.55;color:#4d4a41;font-weight:400;',           text: "De gewone tekst die de meeste pagina's draagt. Gebruik Warm 800 op papier; volle Ink wordt te zwaar.",    meta: '16 / 1.55 · 400' },
];

export const toneRules: [string, string][] = [
  ['— Persoon',      'Tweede persoon: jij, jouw, we, ons. Spreek direct, niet via een omweg.'],
  ['— Hoofdletters', 'Sentence case. Titels niet als Title Case. Eyebrows in uppercase, alléén in mono.'],
  ['— Emoji',        'Nee. Het merk is niet emoji-gedreven. In interne Slack mag het, in product en site niet.'],
];

export const voiceExamples = [
  { do: true,  nl: '"We bouwen \'m zo dat je hem morgen aan je buurjongen kan geven en die er ook wat van bakt."',                                               en: "EN — We build it so you could hand it to the neighbour's kid tomorrow and they'd still ship." },
  { do: false, nl: '"Onze proprietary cloud-native AI-stack democratiseert digitale transformatie voor het MKB."',                                              en: "EN — Our proprietary cloud-native AI stack democratises digital transformation for SMBs." },
  { do: true,  nl: '"WordPress, met een visuele editor. Saai? Misschien. Maar over vijf jaar werkt het nog steeds — en iedere developer kan eraan sleutelen."', en: "EN — WordPress, with a visual editor. Boring? Maybe. But it'll still work in five years, and any developer can pick it up." },
  { do: false, nl: '"Onze AI-gedreven oplossing transformeert uw bedrijfsprocessen middels next-gen synergie."',                                                en: "EN — Our AI-driven solution transforms your business through next-gen synergy." },
  { do: true,  nl: '"We verkopen geen ChatGPT-licenties. We kijken eerst waar AI in jouw bedrijf écht iets oplost — en waar het in de weg zit."',               en: "EN — We don't resell ChatGPT licences. We figure out where AI actually solves something — and where it gets in the way." },
];

export const colophonMeta: [string, string][] = [
  ['Document',   'Arsene Huisstijlhandleiding'],
  ['Datum',      '28 mei 2026'],
  ['Onderhoud',  'Arsene · brand@arsene.nl'],
  ['Vragen',     'info@arsene.nl'],
  ['Typografie', 'Geist & Geist Mono'],
];

export const taglines = [
  { nl: 'Alles kan.',                            en: "EN — Anything's possible.",                    note: 'Open, optimistisch, heel Nederlands. Voorkeur voor home-hero.' },
  { nl: 'Jij de sleutels.\nWij het zware werk.', en: "EN — You keep the keys. We do the heavy lifting.", note: 'Meest letterlijk aan de positionering. Voor uitleg-context.' },
  { nl: 'Software op jouw voorwaarden.',         en: "EN — Software on your terms.",                 note: 'Helder. Maakt het no-lock-in-statement.' },
  { nl: 'Bouw mee, beheer zelf.',                en: "EN — Build along. Run it yourself.",           note: 'Actief, samenwerkend. Voor case-pages en aanbiedingen.' },
  { nl: 'Klein bedrijf,\nechte infrastructuur.', en: "EN — Small business. Real infrastructure.",    note: "Tegen het 'speelgoed-software'-stigma in MKB." },
  { nl: 'Geen lock-in.\nGeen onzin.',            en: "EN — No lock-in. No nonsense.",                note: 'Punchy, een tikkeltje brutaal. Voor sales-context.' },
];
