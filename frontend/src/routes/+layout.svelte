<script lang="ts">
	import NavButton from '$components/NavButton.svelte';
	import UserButton from '$components/UserButton.svelte';
	// import { writable } from 'svelte/store';
	// import { getContext } from 'svelte';
	import '../app.css';
	import type { LayoutData } from './$types';

	export let data: LayoutData;
	$: loggedIn = data.loggedIn;
	// const $loggedIn = data.loggedIn;
	// TBD: check if this is correct
	// TBD: move to store?
	// const loggedIn = writable(false);
	// console.log(loggedIn)
</script>

<!-- <nav class="p-2 space-x-4">
	<a href="/">
		<button
			type="button"
			class="bg-blue-400 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
		>
			Home
		</button>
	</a>
	<a href="/playground">Playground</a>
	<a href="/recipe">Recipe</a>
	<a href="/user">User</a>
</nav> -->

<nav class="p-2 mx-2">
	<div class="flex w-full flex-wrap items-center justify-between">
		<div class="flex-grow space-x-4">
			<NavButton url="/" link="Home" />
			<NavButton url="/playground" link="Playground" />
			<NavButton url="/recipe" link="Recipe" />
		</div>
		<div class="flex space-x-4">
			<!-- <NavButton url="/user" link="User" /> -->
			{#if !loggedIn}
				<NavButton url="/register" link="Register" invert />
				<NavButton url="/login" link="Login" />
			{:else}
				<UserButton />
				<!-- might just redirect to /home and delete session information -->
				<NavButton url="/logout" link="Logout" />
			{/if}
		</div>
	</div>
</nav>

<main>
	<slot />
</main>
