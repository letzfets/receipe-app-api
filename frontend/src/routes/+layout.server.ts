// import type { LayoutServerLoad } from './$types';
// import type { User } from 'src/types.d.ts';
// import { user_store } from '$lib/stores';

// export const load: LayoutServerLoad = async ({ cookies }) => {
// 	// let authenticated = false;
// 	if (cookies.get('accessToken')) {
// 		// authenticated = true;
// 		// user_store.subscribe((user:User) => user.loggedIn = true);
// 	} else {
// 		// authenticated = false;
// 		// user_store.subscribe((user:User) => user.loggedIn = false);
// 	}
// 	// const user = {
// 	// 	loggedIn: authenticated
// 	// };
// 	let user:User | undefined;
// 	user_store.subscribe((user_from_store:User) => {
// 		console.log(user_from_store);
// 		user = user_from_store
// 	});
// 	return user;
// };
