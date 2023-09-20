<script lang="ts">
	export const ssr = false;
	import UserForm from '$components/UserForm.svelte';

	export let form;
</script>

<UserForm />

{#if form?.status === 200}
	<code><pre>{JSON.stringify(form.body.userCreated, null, ' ')}</pre></code>
{/if}
