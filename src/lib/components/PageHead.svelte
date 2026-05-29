<script lang="ts">
  let { title, dark = false }: { title: string; dark?: boolean } = $props();
</script>

<div class="page__head flex justify-between items-center font-mono text-[8pt] tracking-[0.08em] uppercase {dark ? 'text-[rgba(217,232,228,0.55)]' : 'text-warm-600'}">
  <div class="inline-flex items-baseline gap-1 font-sans tracking-[-0.03em] font-semibold text-[10pt] {dark ? 'text-teal-fg' : 'text-ink'}">
    arsene<span class="w-1.5 h-1.5 rounded-full bg-mint ml-px inline-block translate-y-[-0.5px]"></span>
  </div>
  <div>{title}</div>
</div>
