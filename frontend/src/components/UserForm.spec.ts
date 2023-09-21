import { describe, test, expect } from 'vitest';
import { render, screen } from '@testing-library/svelte';
import UserForm from './UserForm.svelte';

describe('Login form', () => {
	test.todo('should have a email and password fields', () => {
		expect(1).toBe(1);
	});
	test.todo('should not have a name field', () => {});
	test.todo('should have a login button', () => {});
});

describe('Register form', () => {
	render(UserForm);
	test('should have a email, password  and name fields', () => {
		// const name = screen.getByRole('input', { name: /name/i });
		// const email = screen.getByRole('input', { name: /email/i });
		// const password = screen.getByRole('input', { name: /password/i });
		const name = screen.getByLabelText('Full name');
		const email = screen.getByLabelText('Email address');
		const password = screen.getByLabelText('Password');

		expect(name).toBeTruthy();
		expect(email).toBeTruthy();
		expect(password).toBeTruthy();
	});
	test('should have a register button', () => {
		const register = screen.getByRole('button');
		expect(register.innerHTML).toContain('Sign up');
	});
});

describe('User form', () => {
	test.todo('should have prefilled email, password  and name fields', () => {
		expect(1).toBe(1);
	});
});
