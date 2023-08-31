FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
# COPY svelte.config.ts ./
# consider copying svelte.config.ts and other files (e.g. tsconfig.json) already in previous step - as npm install seems to call npm run prepare
RUN npm install
COPY . .
RUN npm run prepare && npm run build


FROM node:20-alpine
COPY --from=build /app/build /app/
COPY --from=build /app/package*.json /app/
EXPOSE 3000
USER node
CMD ["node", "/app/index.js"]
