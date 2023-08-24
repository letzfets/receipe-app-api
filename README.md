# receipe-app-api

## Backend:
Receipe API project learning Django Rest Framework and more

Following along with [Vuild a Backend REST API with Python & Django](https://www.udemy.com/course/django-python-advanced/learn/lecture/) 

### Codechecker:

[Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-04-create-python-requirements-file/)

## Frontend

My own creation - trying to add a frontend ina JavaScript framework

# Docker commands:

## Building:

````
docker build .
docker-compose build .
````

## Running various tools
for running backend app (check with backend folder configuration):
````
docker-compose run --rm backend sh -c "python manage.py collectstatic"
````

for running linting (untested):
````
docker-compose run --rm backend sh -c "flake8"
````

for unit testing: using django test *suite*
````
docker-compose run --rm backend sh -c "python manage.py test"
````

## Creating python project:
```
docker-compose run --rm backend sh -c "django-admin startproject app ."
```

## Creating svelte project:

First build a node container with only
```
FROM node:20
WORKDIR /app
```
in the Dockerfile.

Then build the container with `docker build -t frontend --progress=plain .` in the frontend directory.

Then add svelte:

```
docker-compose run --rm frontend sh -c "npm create svelte@4.2.0"
```

Then adding

```
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["node", "./build/index.js"]
```

to Dockerfile.

Add svelte node adapter in frontend directory: `docker run -it -w /app --mount type=bind,src="$(pwd)",target=/app frontend npm i -D @sveltejs/adapter-node`
or through compose-file in root directory of project: `docker-compose run -rm frontend npm i -D @sveltejs/adapter-node`

Build the container with `docker build -t frontend --progress=plain .` and run it with `docker run -p 3000:3000 frontend`

## Starting a service
````
docker-compose up
````

## Combing frontend and backend in one repo:

based on [How to configure Docker with two containers: Frontend and Backend](https://patrickdesjardins.com/blog/docker-nodejs-frontend-backend)

# Github Actions

Find actions in [Github Marketplace](https://github.com/marketplace/actions/)

docker-compose is preinstalled in ubuntu!



