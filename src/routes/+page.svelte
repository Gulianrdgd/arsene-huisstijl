<script lang="ts">
  import PageCover       from '$lib/components/PageCover.svelte';
  import PageIntro       from '$lib/components/PageIntro.svelte';
  import PageWoordmerk   from '$lib/components/PageWoordmerk.svelte';
  import PageBeeldmerk   from '$lib/components/PageBeeldmerk.svelte';
  import PageKleur       from '$lib/components/PageKleur.svelte';
  import PageTypografie  from '$lib/components/PageTypografie.svelte';
  import PageToon        from '$lib/components/PageToon.svelte';
  import PageDetailtaal  from '$lib/components/PageDetailtaal.svelte';
  import PageToepassingen from '$lib/components/PageToepassingen.svelte';
  import PageTaglines    from '$lib/components/PageTaglines.svelte';
  import PageColofon      from '$lib/components/PageColofon.svelte';
  import { exportPdf }   from '$lib/exportPdf';

  let exporting = $state(false);

  async function handleExport() {
    exporting = true;
    await exportPdf();
    exporting = false;
  }
</script>

<button
  onclick={handleExport}
  disabled={exporting}
  class="fixed bottom-6 right-6 z-50 inline-flex items-center gap-2 bg-teal-deep text-teal-fg font-sans font-semibold text-[11pt] px-5 py-2.5 rounded-sm shadow-lg hover:bg-ink transition-colors disabled:opacity-50 disabled:cursor-wait"
>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
  </svg>
  {exporting ? 'Exporteren…' : 'Exporteer PDF'}
</button>

<div class="book bg-warm-400">
  <PageCover />
  <PageIntro />
  <PageWoordmerk />
  <PageBeeldmerk />
  <PageKleur />
  <PageTypografie />
  <PageToon />
  <PageDetailtaal />
  <PageToepassingen />
  <PageTaglines />
  <PageColofon />
</div>
