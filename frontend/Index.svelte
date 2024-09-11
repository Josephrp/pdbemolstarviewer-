<script lang="ts">
  import { onMount } from "svelte";
  import { Block } from "@gradio/atoms";
  import { StatusTracker } from "@gradio/statustracker";
  import { FileData } from "@gradio/upload";
  import type { Gradio } from "@gradio/utils";
  import PDBeMolstarPlugin from "pdbe-molstar/build/pdbe-molstar-plugin";

  export let gradio: Gradio<{
    change: never;
  }>;

  export let value: FileData | null = null;
  export let label: string = "";
  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = true;
  export let loading_status: { status: "pending" | "complete" | "error"; message?: string } | null = null;

  let viewerContainer: HTMLElement;
  let viewerInstance: any;

  onMount(() => {
    viewerInstance = new PDBeMolstarPlugin();
  });

  $: if (value && viewerContainer) {
    const options = {
      customData: {
        url: value.data,
        format: "pdb",
      },
      bgColor: "white",
    };
    viewerInstance.render(viewerContainer, options);
  }
</script>

<Block {visible} {elem_id} {elem_classes}>
  {#if label}
    <label for={elem_id}>{label}</label>
  {/if}

  <div bind:this={viewerContainer} style="width: 100%; height: 400px;"></div>

  {#if loading_status}
    <StatusTracker {...loading_status} />
  {/if}
</Block>

<style>
  label {
    display: block;
    margin-bottom: 4px;
  }
</style>