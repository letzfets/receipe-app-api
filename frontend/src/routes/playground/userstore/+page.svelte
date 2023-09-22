<script lang="ts">
	import { user_store } from '$lib/stores';
	const logUserStore = () => {
		console.log($user_store);
	};
</script>

<button class="bg-blue-400 rounded m-4 p-2" on:click={logUserStore}
	>Current $user_store -> console</button
>
<code><pre>{JSON.stringify($user_store, null, ' ')}</pre></code>
