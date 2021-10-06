# Davee's Django Rest API Template

## Author: Davee Sok

## Links & Resources

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Create Custom User Model](https://testdriven.io/blog/django-custom-user-model/)

## Overview/ Motivation

Starting up a Django api can be time consuming. This template is meant to get up and running fast. Once all the wiring is done, you can make modifications to your models and tests as needed.

## Tools & Dependencies

- Django
- Django Rest Framework
- Black
- Docker
- psycopg2-binary

## Getting Started

#### 1. Click on "Use this template" and create your repo

#### 2. Clone your repo and install dependencies

```iterm
cd into your repo
poetry shell
poetry install
```

#### 3. Create a New Secret Key by running the following command in the terminal:

```iterm
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

#### 4. Add new key to settings.py line 23

```python
SECRET_KEY = "django-insecure-INSERT_NEW_SECRET_KEY_HERE"
```

#### 5. Replace all occurences of "Xxxxx" and "xxxxx" with your new app name

- rename "xxxxx" folder to your new app name(use lower case). Example: xxxxx -> blog
- Do a global search of "Xxxxx" and replace all occurences with your app name
  - (For this step, app name needs to be a capital word) Example: Xxxxx -> Blog
  - Make sure to select "Match Case" option. [Aa]
  - (There will only be 29 matches. If you see 44, you didn't check your case)
- Do a global search of "xxxxx" and replace all occurences with your app name
  - (For this step, app name needs to be a lower cased) Example: xxxxx -> blog
  - Make sure to select "Match Case" option. [Aa]
  - (There will only be 15 matches. If you see a differnt number, you didn't check your case)

#### 6a. If you want to run with docker, run the following commands:

```iterm
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

#### 6b. If you want to run in just the terminal, run the following commands:

```iterm
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Commands To Know

#### Docker:

```python
docker-compose -d
docker-compose up
docker-compose up --build
docker-compose down
docker-compose stop
docker-compose start
docker-compose restart
docker-compose logs
```

#### Httpie Commands through terminal:

```python

# This signs us in and grabs access and refresh tokens
http POST :8000/api/token/ username='admin@gmail.com' password='admin'

# This adds our access token to the headers in our request. Gets all blogs
http GET :8000/api/v1/blog/ 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Gets One Item with pk=4
http GET :8000/api/v1/blog/4 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'

# Deletes One Item with pk=3
http DELETE :8000/api/v1/blog/3 'Authorization: Bearer ADD_ACCESS_TOKEN_HERE'
```

#### Other:

```python
poetry export -f requirements.txt -o requirements.txt --without-hashes
python manage.py collectstatic -> whitenoise command to add static files
```

---

### Extra Notes

This project makes use of a custom user that over writes django's default user model. When you create new models that need to reference user as a foreign key, you need to make the following changes:

```python
# Old Way

from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

# ----------------------------------- New Way -----------------------------------

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

```

In your tests, you would still use get_user_model()
