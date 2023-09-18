import { getBackend } from '$lib/backend';

export const load = async () => {
	const schema = await getBackend('http://host.docker.internal:8000/api/schema?format=json');
	// console.log(data);
	return schema;
	// return {
	//     data: schema
	// };
	// if (schema === null) {
	//     return error(401, 'Unauthorized');
	// }
	// return {
	//     props: {
	//         schema: schema
	//     }
	// };
};
