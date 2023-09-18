<script>
	import '../app.css';
</script>

<nav class="p-2 space-x-4">
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
</nav>

<slot />
