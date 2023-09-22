import type { LayoutServerLoad } from './$types';
import { getBackend } from '$lib/backend';
import type { User } from 'src/types.d.ts';
// import { user_store } from '$lib/stores';

export const load: LayoutServerLoad = async ({ cookies }) => {
	// let authenticated = false;
    let user:User = {
        loggedIn: false,
        email: '',
    }
	if (cookies.get('accessToken')) {
		// authenticated = true;
        user = await getBackend('/api/user/me', cookies.get('accessToken'))
        // console.log('user retrieved from backend:');
        // console.log(user);
        user.loggedIn = true;
		// user_store.set(user);
		//user_store.subscribe((user:User) => user.loggedIn = true);
	} 
    // else {
	// 	// user_store.set(user);
	// 	// authenticated = false;
	// 	// user_store.subscribe((user:User) => user.loggedIn = false);
	// }
	// const user = {
	// 	loggedIn: authenticated
	// };
	// let user:User | undefined;
	// user_store.subscribe((user_from_store:User) => {
	// 	console.log(user_from_store);
	// 	user = user_from_store
	// });
	return user;
};
