// handle the backend API calls

const host = 'http://host.docker.internal:8000';

export const getBackend = async (url: string) => {
	const response = await fetch(host + url);
	const data = await response.json();
	return data;
};

// TBD: POST to backend
// TBD: PUT to backend
// TBD: DELETE from backend

// TBD: write test for getUser
// export const getUser = async () => {
//     await getBackend('https://backend/api/user');
// };
