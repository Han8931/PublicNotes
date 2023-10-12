---
tags: web, django, python, deployment
---
# Overview
To make our site available on the Internet where everyone can see it, we need to deploy our code to an external server and database. This is called putting our code into production. Local code lives only on our computer; production code lives on an external server available to everyone.

0. `python -m pip install gunicorn django-heroku`

1. Create a file:
- `runtime.txt` 
	- type your python version e.g., `python-3.7.4`
- `Procfile`
	- `web: gunicorn <project_name>.wsgi:application --log-file -`
2. Requirements:
	- `pip freeze > requirements.txt`
3. `settings.py`
	- `import django_heroku`
	- `import dj_database_url`
	- `django_heroku.settings(locals())`
	- `ALLOWED_HOSTS = [mysite.com]`
4. Run `heroku`