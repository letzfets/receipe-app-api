<script lang="ts">
	export let url: string;
	export let link: string;
</script>

<a href={url}>
	<button
		type="button"
		class="bg-blue-400 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	>
		{link}
	</button>
</a>
