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
## Backend

### Creating python project:
```
docker-compose run --rm backend sh -c "django-admin startproject app ."
```

## Frontend

### Creating svelte project:

First build a node container with only
```
FROM node:20
WORKDIR /app
```
in the Dockerfile.

Then build the container with `docker build -t frontend --progress=plain .` in the frontend directory.

Then add svelte:

```
docker-compose run -f compose.yml -f compose.dev.yml --rm frontend sh -c "npm create svelte@4.2.0"
```

Add svelte node adapter in frontend directory: `docker run -it -w /app --mount type=bind,src="$(pwd)",target=/app frontend npm i -D @sveltejs/adapter-node`
or through compose-file in root directory of project: `docker-compose run -f compose.yml -f compose.dev.yml -rm frontend npm i -D @sveltejs/adapter-node`
or after `docker-compose -f compose.yml -f compose.dev.tml up -d`: `docker-compose run <image-name> npm i -D <...>`

Build the container with `docker build -t frontend --progress=plain .` and run it with `docker run -p 3000:3000 frontend`

### Updating Frontend:

`docker compose -f compose.yml -f compose.cicd.yml run --rm frontend sh -c "npm update"`


## Starting the dev environment
````
docker-compose -f compose.yml -f compose.dev.yml up -d
````


## Combing frontend and backend in one repo:

based on [How to configure Docker with two containers: Frontend and Backend](https://patrickdesjardins.com/blog/docker-nodejs-frontend-backend)

# Github Actions

Find actions in [Github Marketplace](https://github.com/marketplace/actions/)

docker-compose is preinstalled in ubuntu!

# Testing:

## Backend

- unittest library
- django adds: test client, simulate authentication, temporary database
- django restframework adds: API test client

add `tests.py` (module) OR `tests-directory` (prefix every module with `tests_`).
Tests directory must contain `__init__.py`

Test database: django creates a specific database for tests (and deletes it after every test)

Test classes:
- SimpleTestCase (without database)
- TestCase (database included)

prefix test-methods with `test_`

### Test Driven Development (TDD)

First write test and then add the development

### Mocking

- override or change behavior of dependencies
- avoid unintended side effects
- isolate code being tested

benefits:
- avoid relying on external services: might not available at test time
- avoid unintended consequences: like sending an email for every test or overloading external servicers in another way

Example: 
- user registers -> gets welcome email. "Mock" the sending of the email.
- check database and then sleep for a while

Use unittest.mock
- MagicMock/Mock: replace real objects
- patch: overrides code for tests