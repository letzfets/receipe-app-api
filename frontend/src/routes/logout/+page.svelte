<script lang="ts">
	import { user_store } from '$lib/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import type { PageData } from './$types';
	export let data: PageData;

	$user_store = null
	onMount(() => goto('/'));
</script>
