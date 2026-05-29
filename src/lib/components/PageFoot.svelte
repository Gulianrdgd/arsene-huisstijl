<script lang="ts">
  let { page, dark = false }: { page: string; dark?: boolean } = $props();
</script>

<div class="page__foot flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase {dark ? 'text-[rgba(217,232,228,0.55)]' : 'text-warm-600'}">
  <div>Arsene Huisstijl</div>
  <div>{page}</div>
</div>
