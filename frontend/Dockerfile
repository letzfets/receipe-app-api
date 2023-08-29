FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
# COPY .svelte-kit/ .svelte-kit/
RUN npm install && ls -la node_modules/
COPY . .
RUN npm run build
EXPOSE 3000
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