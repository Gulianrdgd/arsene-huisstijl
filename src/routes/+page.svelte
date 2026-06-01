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
</script>

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
