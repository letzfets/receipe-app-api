// handle the backend API calls

const host = 'http://host.docker.internal:8000';

//TBD: GET from backend
export const getBackend = async (url: string) => {
	const response = await fetch(host + url);
	// console.log(response);
	// return response;
	const data = await response.json();
	console.log(data);
	return data;
};

// TBD: POST to backend
// TBD: PUT to backend
// TBD: DELETE from backend

// TBD: write test for getUser
// export const getUser = async () => {
//     await getBackend('https://backend/api/user');
// };
