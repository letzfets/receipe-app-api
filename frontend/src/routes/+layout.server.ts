import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ cookies }) => {
	let authenticated = false;
	if (cookies.get('accessToken')) {
		authenticated = true;
	} else {
		authenticated = false;
	}
	const user = {
		loggedIn: authenticated
	};
	return user;
};
