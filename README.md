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

### Testing web requests

Django rest framework API client
- based on Django's TestClient
- make requests
- check result
- override authentication

`from rest_framework.test import APIClient`

check status code: `self.assertEqual(res.status_code, '200')`

### Common testing problems:

number of tests ran not correct
- missing __init__.py in tests/ directory
- indentation of test cases
- missing `test` prefix for test methods name (those can be used as helper functions in the test file)
- import error when running test: Is this module globally installed: both `tests`directory and `tests.py` exist in app

## Frontend

[How to Do Test-Driven Development with Svelte and Vitest – A Project-Based Tutorial](https://www.freecodecamp.org/news/how-to-do-test-driven-development-with-svelte-and-vitest/)

configure vitest in `vite.config.js`or override it with `vitest.config.js`

# Adding the database:

PostgreSQL
- popular open source
- free
- integrates well with Django

using Docker Compose for configuration,
- so its defined with project and other developers can also use it
- persistent data using volumes
- handles network configuration
- handles environment variable configuration

Architecture:
- Docker compose adds another service: database
- backend need to `depends_on` database -> still needs handling of database race condition

Volumes in docker compose:
- persist data
- maps directory in container to local machine
- using a named volume (that is at top)

Configuring the database:
- configure django: how to connect to database
- install database adaptor dependencies
- update python requirements to include postgres adaptor
Django needs to know:
- database engine
- hostname / ip of database's host
- port (usually 5432)
- database name
- credentials: username and password
everything goes into `settings.py` and pull everything from environment variables

environment variables
- can be easily passed to docker,
- used in prod and dev
- single place to configure project
- easy to do with python
code to pull environment variables in python `os.environ.get('<var-name>')``

package *psycopg2*: package needed for django to connect to database
- most popular postgres adaptor for python
- supported officially by django

installation options for psycopg2:
- psycopg2-binary, not optimized for production
- psycopg2, e.g. with pip, compiled from source, needs dependencies but optimizes for machine - but easy with docker

dependencies for psycopg2:
- c compiler
- python3-dev
- libpq-dev
in alpine called
- postgresql-client
- build-base
- postgresql-dev
- musl-dev

best practice in docker: clean-up dependencies after install in Dockerfile (keep at minimum and light weight)!

