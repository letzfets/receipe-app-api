<script lang="ts">
	import Guard from '$components/Guard.svelte';
	import { user_store } from '$lib/stores.js';
	import NavButton from '$components/NavButton.svelte';
</script>

<Guard>
	<h1 class="m-5 text-3xl text-primary text-center">
		Welcome inside {$user_store?.name} - this is your Dashboard
	</h1>
	<NavButton url="/recipe" link="Recipe" />
</Guard>
