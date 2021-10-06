# Cookie Stand Api V2

## Author: Davee Sok

## Links & Resources

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Create Custom User Model](https://testdriven.io/blog/django-custom-user-model/)

## Overview/ Motivation

Create a Cookie Stand API

## Tools & Dependencies

- Django
- Django Rest Framework
- Black
- Docker
- psycopg2-binary

## Commands To Know

```iterm
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

```iterm
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Docker

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

#### Httpie Commands through terminal

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

#### Other

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
