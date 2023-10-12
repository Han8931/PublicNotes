---
tags: web, django, python
---
# Setup
- `python3 -m venv <project>`
- `source <project>/bin/activate`
- `pip install django`

# First Project
- `django-admin startproject <project>`
- `python3 manage.py runserver`
	- The default Django development server is listening at 8000.

- It's worth pausing here to explain why you should add a period to the end of the previous command. If you just run `django-admin startproject django_project` then by default Django will create a directory structure inside another dir with the same name. To avoid this duplicate, put a period at the end of the command.
- Now let's confirm everything is working by running Django’s internal web server via the `runserver` command. This is suitable for local development purposes, but when it comes time to deploy our project’s online we will switch to a more robust WSGI server like _Gunicorn_.

## Initial Directory Structure
- `__init__.py` this indicates that the files in the folder are part of a Python package. 
- `asgi.py`: Allows for an optional Asynchronous Server Gateway Interface to be run.
- `settings.py`: controls our Django project's overall settings
- `urls.py`: tells Django which pages to build in response to a browser or URL request.
- `wsgi.py`: stands for Web Server Gateway Interface which helps Django serve our eventual web pages. 

Note that `manage.py` file is not part of our project but is used to execute various Django commands such as running the local web server or creating a new app. 

If we run our `manage.py` by using a `runserver` command, then we will get some error saying that `unapplied migrations`. This tells us we haven't yet migrated our initial database. 

# WebDev Concepts

## HTTP Request/Response Cycle
HTTP (Hypertext Transfer Protocol)20 was initially created by Tim Berners-Lee in 1989 and is the foundation of the World Wide Web. A network protocol is a set of rules for formatting and processing data. It is like a common language for computers that allows them to communicate with one another even if they are located on opposite sides of the earth and have vastly different hardware and software.

HTTP is a request-response protocol that works in a client-server computing model. Every time you visit a webpage an initial "request" is sent by the "client" (ie your computer) and a "response" is sent back by a "server." The client doesn’t have to be a computer though, it could also be a mobile phone or any internet-connected device. But the process is the same: an HTTP request is sent to a URL by a client and a server sends back an HTTP response.

Ultimately, all a web framework like Django does is accept HTTP requests to a given URL and return a HTTP response containing the information necessary to render a webpage. That’s it. Generally this process involves identifying the proper URL, connecting to a database, adding some logic, applying style with HTML/CSS/JavaScript/static assets, and then return the HTTP response. That’s it.

# Create an App
Django uses the concept of projects and apps to keep code clean and readable. A single top-level Django project can contain multiple apps. Each app controls an isolated piece of functionality.

To add a new app, go to the command line and quit the running server with `<C-c>`. Then use the `startapp` command followed by the name of our app which will be pages.
- `python manage.py startapp pages`

# Template
Every web framework needs a convenient way to generate HTML files and in Django the approach is to use templates: individual HTML files that can be linked together and also include basic logic.

Django has a minimal templating language for adding links and basic logic in our templates. **Template tags** take the form of `{% something %}` where _the "something" is the template tag itself_. You can even create your own custom template tags, though we won't do that in this book.

# Test
-  SimpleTestCase
- TestCase
- TransactionTestCase
- LiveServerTestCase