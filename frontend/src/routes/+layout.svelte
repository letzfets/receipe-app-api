<script lang="ts">
	import NavButton from '$components/NavButton.svelte';
	import UserButton from '$components/UserButton.svelte';
	import '../app.css';
	// import type { LayoutData } from './$types';
	import { user_store } from '$lib/stores';

	$: console.log($user_store);
	// // export let data: LayoutData;
	export let loggedIn = false;
	if($user_store){
		loggedIn = $user_store.loggedIn || false;
	}
	// if(){
	// 	console.log(data);
	// 	loggedIn = true
	// }
		
	// console.log(data);
	// $: loggedIn = data.loggedIn;
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

<button class="bg-blue-400 rounded m-4 p-2" on:click={console.log($user_store)}>Current $user_store</button>
<code><pre>{JSON.stringify($user_store, null, ' ')}</pre></code>