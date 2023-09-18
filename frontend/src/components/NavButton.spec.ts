import { describe, test, expect } from 'vitest';
import { render, fireEvent, screen } from '@testing-library/svelte';
import NavButton from './NavButton.svelte';

describe('NavButton', () => {
	test('should navigate to new URL when clicked', async () => {
		const newUrl = '/new-url';
		render(NavButton, { props: { href: newUrl } });

		const button = screen.getByRole('button');

		await fireEvent.click(button);

		expect(window.location.pathname).toContain(newUrl);
	});
});
