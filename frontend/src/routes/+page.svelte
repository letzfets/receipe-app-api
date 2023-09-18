<script lang="ts">
	import { parse, stringify } from 'postcss';

	// /** @type {import('./$types').PageData} */
	import type { PageData } from './$types';
	export let data: PageData;
	// console.log(data.Response)
</script>

<h1 class="text-xl text-center">
	Welcome to SvelteKit - prepared setup for frontend for receipe app
</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<code>{JSON.stringify(data)}</code>
