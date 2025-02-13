<script>
    import Button from "$lib/interactive/button.svelte";
</script>

<div class="text-right max-h-min my-auto">
    <Button on:click={()=>{alert("<logging in>")}}><p>Log in.</p></Button>
</div>
