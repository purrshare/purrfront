<script>
	let buttonProps = { class:[$$restProps.class] };
</script>

<button on:click on:mouseover on:focus on:mouseenter on:mouseleave {...buttonProps} 
        class="p-2 m-2 rounded-xl border-2
               border-gray-800 bg-slate-200 hover:bg-slate-300 active:bg-slate-400
               ">
    <slot />
</button>
