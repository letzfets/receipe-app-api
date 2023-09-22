<script lang="ts">
	// import { goto } from '$app/navigation';
	export const ssr = false;
	import UserForm from '$components/UserForm.svelte';

	export let form;
	if (form?.status === 200) {
		// console.log(form.body.userCreated);
		// goto('/');// TBD: use onMount or redirect?
	}
</script>

<UserForm />

<!-- {#if form?.status === 200}
	<code><pre>{JSON.stringify(form.body.userCreated, null, ' ')}</pre></code>
{/if} -->
