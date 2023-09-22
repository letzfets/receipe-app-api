<script lang="ts">
	import { count } from '$lib/stores';

	const add = () => {
		count.update((n) => n + 1);
	};
	const subtract = () => {
		count.update((n) => n - 1);
	};
	const reset = () => {
		count.set(0);
	};
</script>

<p class="text-8xl m-10">{$count}</p>
<br />
<button class="bg-blue-400 m-4 p-2" on:click={add}>+</button>
<button class="bg-blue-400 m-4 p-2" on:click={subtract}>-</button>
<button class="bg-blue-400 m-4 p-2" on:click={reset}>reset</button>
