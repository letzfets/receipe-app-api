// Tests for generic backend functions
import { describe, it, expect, beforeAll, afterAll, afterEach } from "vitest";
import { setupServer } from "msw/node";
import { rest } from "msw";
import { waitForBackend } from "./generic";

const server = setupServer();
beforeAll(() => server.listen());
afterAll(() => server.close());
afterEach(() => server.resetHandlers());

describe("Tests for generic backend functions", () => {
    it.todo("should wait for backend", async () => {
        server.use(
            rest.get("https://backend/health", (req, res, ctx) => {
                return res(
                    ctx.status(200),
                    ctx.delay(2000)
                    );
            })
        );
        const result = await waitForBackend();
        expect(result).toBe(true);
    })
})