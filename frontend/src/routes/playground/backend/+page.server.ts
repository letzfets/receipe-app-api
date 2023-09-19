import { getBackend } from '$lib/backend';

// TBD: add type PageServerLoad here?
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
