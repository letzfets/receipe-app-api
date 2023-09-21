// tests for backend functions
import { describe, test, expect, beforeAll, afterAll } from 'vitest';
import { setupServer } from 'msw/node';
import { rest } from 'msw';
import { getBackend, postBackend } from './backend';

const dummyResponse = { data: 'test' };

const server = setupServer(
	rest.get('http://host.docker.internal:8000/api/schema', (req, res, ctx) => {
		req.url.searchParams.set('format', 'json');
		return res(ctx.json(dummyResponse));
	})
);

beforeAll(() => server.listen());
afterAll(() => server.close());

describe('GET data from backend', () => {
	test('should get data from backend', async () => {
		const data = await getBackend('/api/schema?format=json');
		expect(data).toEqual(dummyResponse);
	});
});

describe('POST data to backend', () => {
	test('should post data to backend', async () => {
		const payload = {
			name: 'User One',
			email: 'user@example.com',
			password: 'secretPassword'
		};
		server.use(
			rest.post('http://host.docker.internal:8000/api/user/create', (req, res, ctx) => {
				// return res((res) => {
				// 	res.status = 200
				// 	res.body = JSON.stringify({
				// 		name: payload.name,
				// 		email: payload.email
				// 	})
				// 	return res
				// }
				return res(
					ctx.status(200),
					ctx.json({
						name: payload.name,
						email: payload.email
					})
				);
			})
		);

		const response = await postBackend('/api/user/create', payload);
		// console.log(response);
		// expect(response.status).toBe(200);
		expect(response).toContain({ name: 'User One', email: 'user@example.com' });
	});
	test.todo('should read the posted data back from the backend');
});
