<script lang="ts">
	import { goto } from '$app/navigation';
	import { user_store } from '$lib/stores.js';
</script>

<!-- TBD: turn this routeguard into a component -->
{#if $user_store?.loggedIn}
	<h1 class="m-5 text-3xl text-primary text-center">
		Welcome inside {$user_store?.name} - this is your Dashboard
	</h1>
{:else}
	{goto('/login')}
{/if}
