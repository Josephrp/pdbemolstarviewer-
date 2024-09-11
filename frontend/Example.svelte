<script lang="ts">
  import { FileData } from "@gradio/upload";

  export let value: FileData;
  export let type: "gallery" | "table";
  export let selected = false;
</script>

<div class:selected>
  {value.orig_name}
</div>

<style>
  div {
    padding: 4px;
    border-radius: 4px;
  }
  .selected {
    background-color: var(--color-accent-soft);
  }
</style>