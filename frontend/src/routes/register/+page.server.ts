import { postBackend } from '$lib/backend';
// import { error } from '@sveltejs/kit';

// TBD: add type PageServerLoad here?
export const actions = {
	default: async ({ cookies, request }) => {
		const data = await request.formData();
		const payload = {
			name: data.get('name')?.toString() || '',
			email: data.get('email')?.toString() || '',
			password: data.get('password')?.toString() || ''
		};
		// console.log(payload)
		const userCreated = await postBackend('/api/user/create/', payload);
		delete payload.name;
		const accessToken = await postBackend('/api/user/token/', payload);
		cookies.set('accessToken', accessToken.token);
		return {
			status: 200,
			body: {
				// message: "user Created",
				userCreated
			}
		};
	}
};
// {
// 	const userCreated = await postBackend('/api/user/create', );

// 	if (schema === null) {
// 		return error(404, 'Unavailable');
// 	}
// 	return schema;
// };
