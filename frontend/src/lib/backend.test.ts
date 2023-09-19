// tests for backend functions
import { describe, test, expect, beforeAll, afterAll } from 'vitest';
import { setupServer } from 'msw/node';
import { rest } from 'msw';
import { getBackend } from './backend';

const dummyResponse = { data: 'test' };

const server = setupServer(
	rest.get('http://host.docker.internal:8000/api/schema?format=json', (req, res, ctx) => {
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
