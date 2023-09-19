import { getBackend } from '$lib/backend';

export const load = async () => {
	const schema = await getBackend('/api/schema?format=json');
	return schema;
	// if (schema === null) {
	//     return error(401, 'Unauthorized');
	// }
	// return {
	//     props: {
	//         schema: schema
	//     }
	// };
};
