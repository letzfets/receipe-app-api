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

### Adding a new app to the python project:
```
docker compose -f compose.yml -f compose.cicd.yml run --rm backend sh -c "python manage.py startapp <ne app name>"
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

## Architecture:
- Docker compose adds another service: database
- backend need to `depends_on` database -> still needs handling of database race condition

Volumes in docker compose:
- persist data
- maps directory in container to local machine
- using a named volume (that is at top)

## Configuring the database:
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


## Database postgresql adaptor
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

## Database configuration
Configuring database in django in settings.py file:
[Reference](https://docs.djangoproject.com/en/4.2/ref/settings/#databases)

## Fixing a database race configuration
docker compose has `depends_on`, which only waits until service has started, but not yet, that the service is running. Solution: make Django wait for db, using a custom Django management command.

Adding a new python app for awaiting the database:
`docker compose -f compose.yml -f compose.cicd.yml run --rm backend sh -c "python manage.py startapp core"`

## Database migrations

### Django Object Relational Mapper (ORM)

is an *abstraction layer for data* to let django handle databse structure and changes.
- Handles table generation, adding columns, and so on.
- also allows to switch databases (within reason): for example switching from postgres to mySQL

### Using the **Object Relational Mapper**:
- define models (done through programming)
- generate migration file (handled by ORM automatically)
- setup the database (handled by ORM automatically)
- store data (handled by ORM automatically)

### Models:

each model
- maps to a table
- contains
    - name
    - fields (represent columns)
    - metadata (relationships between tables)
    - custom python logic (e.g. execute code on every safe or validation)

Model example:
```
class ingredient (`models.Model`):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
```

### Migrations
enable app in `settings.py` and run through `python manage.py makemigrations`:
- checks existing database
- looks for differences of models
- adds new migrations
- at first time running: initial setup of database

afterwards apply the migrations to database by running `python manage.py migrate`
Always run the migration after `wait_for_database`

# Create Django User model

Using default django user model. Django has built in **user authentication**

Framework for basic features:
- registration
- login
- auth

Integrates with Django admin

Default Django user model is foundation of django auth system

Default user model
- uses username instead of email
- not easy to customize

Therefore create a custom user model 
based on `AbstractBaseUser` and `PermissionMixin`

Create custom manager used for CLI integration

Afterwards set AUTH_USER_MODEL in settings.py

Create and run migrations

**AbstractBaseUser**
Provides features for authentication but does not include fields.

**PermissionsMixin**

Support for Django permission system

Includes fields and methods

**Common issue**

- Running migrations before setting custom model: not good. Therefore clear them!
ALWAYS set user model first before running migrations.
- Typos in config
- Indentation in manager or model

## Design custom user model

user fields:
- email (EmailField)
- name (CharField)
- is_active (BooleanField)
- is_staff (BooleanField) -> if true, allows login to django admin

user model manager:
- used to manage objects
- custom logic for creating objects
    - hash passwords
- used by Django CLI
    - create superuser


BaseUserManager
- base class for managing users
- useful helper methods
    - `normalize_email` for storing emails consistently
- Methods to define:
    - `create_user` called when creating user
    - `create_superuser`used by CLI to create a superuser (=admin)

## Implement User model
 
 in `core/models.py`

 Make migrations:
 `docker compose -f compose.yml -f compose.dev.yml run --rm backend sh -c "python manage.py makemigrations"`

 Apply migrations:
 `docker compose -f compose.yml -f compose.dev.yml run --rm backend sh -c "python manage.py wait_for_db && python manage.py migrate"`
=> fails, as migrations ran previously with standard Django user model.

 Therefore clearing data for database:
```
docker compose down
docker volume rm receipe-app-api_dev-db-data
```

After clearing the database, it works:
`docker compose -f compose.yml -f compose.dev.yml run --rm backend sh -c "python manage.py wait_for_db && python manage.py migrate"`

## Creating super user

in command line:

`docker compose -f compose.yml -f compose.dev.yml run --rm backend sh -c "python manage.py createsuperuser"`

# Setup Django Admin

- Graphical User Interface for models
    - Create, Read, Update, Delete (CRUD)
- very little coding required
- needs to be enabled per model in `admin.py`
    - `admin.site.register(<model>)``

Customizing:
- through class based of `ModelAdmin` or `UserAdmin`
- override/ set class variables
- Changing list of objects
    - `ordering`: changing order of items appearance
    - `list_display`: fields to appear in list
- add/update page:
    - `fieldsets` control layout of page
    - `readonly_fields`
- add page:
    - `add_fieldsets`: fields displayed only on add page

# Structuring the frontend

[Understanding the structure of a SvelteKit project](https://www.inow.dev/understanding-the-structure-of-a-svelte-kit-project/)

# API documentation

## Importance of API documentation

Purpose:
- designed for developers
- developers need to know how to use it
- API is only as good as its documentation

What to document:
- everything needed to use the API
- available endpoints
- supported methods, like
    - `GET`
    - `POST`
    - `PUT`
    - `PATCH`
    - `DELETE`
- Format of payloads (input)
    - parameters (f.x. filtering)
    - Post JSON format
- Format of responses (outputs)
    - Response JSON format
- Authentication process

Options for documentation:
- Manual: (drawback: manual updates & risk of not updated documenting)
    - word document
    - markdown
- automated
    - use metadata from code (comments)
    - generate documentation pages

Here:
- Tools for making documentation seamless
- Add documentation for our API, including graphical interface to run tests

## Auto docs with Django REST framework (DRF)

Docs in DRF
- auto generate docs (with third party library)
    - many tools available
    - here `drf-spectacular`
- generates a *schema*
- which allows a browsable web interface
    - can make test requests
    - handle auth

How it works:
1. Generate `schema` file
2. Parse schema in GUI

### OpenAPI Schema

- standard for describing APIs
- popular in industry
- supported by most API documentation tools - here using Swagger
- uses popular formats: YAML/JSON

### Using a schema
- download and run in local or public Swagger instance
- serve swagger with API (makes it interactive)

# Build user API

## User API design

Functionality:
- User registration
- creating an auth token
- viewing and updating user profile

Endpoints:
- `user/create`
    - `POST` register new user
- `user/token`
    - `POST` create a new token: payload contains username and password, returns token
- `user/me`
    - `GET` to view profile
    - `PUT/PATCH` update user profile