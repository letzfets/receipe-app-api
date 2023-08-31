FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json svelte.config.js ./
RUN npm install
COPY . .
RUN npm run build
CMD ["sh" "-c"]

FROM node:20-alpine
COPY --from=build /app/build /app/
COPY --from=build /app/package*.json /app/
EXPOSE 3000
USER node
CMD ["node", "/app/index.js"]
