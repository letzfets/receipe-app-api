<script lang="ts">
	import { goto } from '$app/navigation';
	export const ssr = false;
	import UserForm from '$components/UserForm.svelte';

	export let form;
	// TBD: check if user is logged in (protected route) - this form status check is not enough!
	if (form?.status === 200) {
		// TBD: use onMount or redirect?
		// TBD: redirect to /dashboard after implementation of protected routes
		goto('/dashboard');
	}
</script>

<UserForm />
