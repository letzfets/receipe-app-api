<script lang="ts">
	import NavButton from '$components/NavButton.svelte';
	import UserButton from '$components/UserButton.svelte';
	import '../app.css';
	import type { LayoutData } from './$types';
	import { user_store } from '$lib/stores';

	export let data: LayoutData;
	$user_store = data;
</script>

<nav class="p-2 mx-2">
	<div class="flex w-full flex-wrap items-center justify-between">
		<div class="flex-grow space-x-4">
			<NavButton url="/" link="Home" />
			<NavButton url="/playground" link="Playground" />
			<NavButton url="/recipe" link="Recipe" />
		</div>
		<div class="flex space-x-4">
			<!-- <NavButton url="/user" link="User" /> -->
			{#if !$user_store?.loggedIn}
				<NavButton url="/register" link="Register" invert />
				<NavButton url="/login" link="Login" />
			{:else}
				<UserButton />
				<!-- needs to redirect to /home and delete session information -->
				<!-- TBD: write tests for logout -->
				<NavButton url="/logout" link="Logout" />
			{/if}
		</div>
	</div>
</nav>

<main>
	<slot />
</main>
