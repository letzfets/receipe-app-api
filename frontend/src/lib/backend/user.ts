// Implements interaction with the backend for user related tasks
import { waitForBackend } from './generic';

// TBD: write test for getUser
export const getUser = async () => {
	await waitForBackend();
	return {
		email: 'frontend@ecample.com',
		isActive: true,
		isStaff: false,
		isSuperuser: false
	};
};
