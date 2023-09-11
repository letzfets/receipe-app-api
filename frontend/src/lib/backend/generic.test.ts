// Tests for generic backend functions
import { describe, it, expect } from "vitest";
import { waitForBackend } from "./generic";

describe("Tests for generic backend functions", () => {
    it.todo("should wait for backend", async () => {
        const result = await waitForBackend();
        expect(result).toBe(true);
    })
})