FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json svelte.config.ts ./
# consider copying svelte.config.ts and other files (e.g. tsconfig.json) already in previous step - as npm install seems to call npm run prepare
# COPY .svelte-kit/ .svelte-kit/
RUN npm install
COPY . .
# RUN pwd
# RUN ls -la
RUN npm run prepare && npm run build
# RUN ls -la
# RUN ls -la node_modules
# RUN ls -la build
# CMD ["node", "./build/index.js"]

FROM node:20-alpine
COPY --from=build /app/build /app/
COPY --from=build /app/package*.json /app/
EXPOSE 3000
USER node
CMD ["node", "/app/index.js"]

# FROM nginx:1.25.2-alpine AS production
# COPY --from=build /app/build /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]