// handle the backend API calls
import type { User } from 'src/types.d.ts';

const host = 'http://host.docker.internal:8000';

export const getBackend = async (url: string) => {
	const response = await fetch(host + url);
	const data = await response.json();
	return data;
};

// TBD: POST to backend
export const postBackend = async (url: string, payload: User) => {
	const response = await fetch(host + url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(payload)
	});
	const data = await response.json();
	return data;
};
// TBD: PUT to backend
// TBD: DELETE from backend

// TBD: write test for getUser
// export const getUser = async () => {
//     await getBackend('https://backend/api/user');
// };
