<script lang="ts">
	import { goto } from '$app/navigation';
	export const ssr = false;
	import UserForm from '$components/UserForm.svelte';

	export let form;
	if (form?.status === 200) {
		// TBD: use onMount or redirect?
		// TBD: redirect to /dashboard after implementation of protected routes
		goto('/');
	}
</script>

<UserForm type="signup" />
