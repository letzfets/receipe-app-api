<script lang="ts">
	// /** @type {import('./$types').PageData} */
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<div class="mx-5">
	<h1 class="mb-2 mx-5 mt-0 text-5xl font-medium leading-tight text-primary">
		Getting schema from backend
	</h1>
</div>

<code><pre>{JSON.stringify(data, null, " ")}</pre></code>
