# receipe-app-api

## Backend:
Receipe API project learning Django Rest Framework and more

Following along with [Vuild a Backend REST API with Python & Django](https://www.udemy.com/course/django-python-advanced/learn/lecture/) course

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


# Codechecker:

[Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-04-create-python-requirements-file/)