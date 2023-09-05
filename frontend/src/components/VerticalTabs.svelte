<!-- <script lang="ts">
    let selectedIndex = 0;
    const changeSecondTab = () => {
        selectedIndex = 1;
    }
</script> -->

<div class="vertical-tab-container">
	<ul class="vertical-tab">
		<li>First Tab</li>
        <li>Second Tab</li>
		<!-- <li on:click={() => changeSecondTab()}>Second Tab</li> -->
		<li>Third Tab</li>
	</ul>

	<div class="vertical-tab-content">
        <h2>First Tab Heading</h2>
		<p>
			Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem aut deserunt veniam tempora
			deleniti quos reprehenderit natus. Animi, obcaecati dolorum, culpa, maiores maxime ullam
			soluta unde rerum nihil temporibus quibusdam!
		</p>
        <!-- {#if selectedIndex == 0}
		<h2>First Tab Heading</h2>
		<p>
			Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem aut deserunt veniam tempora
			deleniti quos reprehenderit natus. Animi, obcaecati dolorum, culpa, maiores maxime ullam
			soluta unde rerum nihil temporibus quibusdam!
		</p>
        {:else if selectedIndex == 1}
        <h2>Second Tab Heading</h2>
		<p>...</p>
        {/if} -->
	</div>
</div>

<style>
	.vertical-tab-container {
		display: flex;
		flex-direction: row;
		align-items: center;
		border: 1px solid gray;
		border-radius: 1rem;
	}

	.vertical-tab {
		margin: 0px;
		padding: 3rem;
		list-style: none;
		border-right: 1px solid gray;
	}

	.vertical-tab li {
		margin: 2rem 0;
	}

	.vertical-tab-content {
		flex: 1;
		align-items: center;
	}
</style>
