import { writable } from "svelte/store";
import type { User } from "src/types.d.ts";

export const user_store = writable<User | null>();
export const count = writable<number>(0);