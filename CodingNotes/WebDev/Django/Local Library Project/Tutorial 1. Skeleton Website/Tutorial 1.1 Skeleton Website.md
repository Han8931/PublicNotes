---
tags: web, django, python, local_library
---
# The LocalLibrary website

_LocalLibrary_ is the name of the website that we'll create and evolve over the course of this series of tutorials. As you'd expect, the purpose of the website is to _provide an online catalog for a small local library, where users can browse available books and manage their accounts._

This example has been carefully chosen because it can scale to show as much or as little detail as we need, and can be used to show off almost any Django feature. More importantly, it allows us to provide a _guided_ path through the most important functionality in the Django web framework:
1. In the first few tutorial articles we will define a simple _browse-only_ library that library members can use to find out what books are available. This allows us to explore the operations that are common to almost every website: reading and displaying content from a database.
2. As we progress, the library example naturally extends to demonstrate more advanced Django features. For example we can extend the library to allow users to reserve books, and use this to demonstrate how to use forms, and support user authentication.

## Creating the Project

- Initialize the project by `django-admin startproject locallibrary`
- The `django-admin` tool creates a folder/file structure as follows:
```
locallibrary/
    manage.py
    locallibrary/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

The _locallibrary_ project sub-folder is the entry point for the website:
- The **manage.py** script is used to _create applications_, work with databases, and start the development web server.
- **__init__.py** is an empty file that instructs Python to treat this directory as a Python package.
- **settings.py** contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.
- **urls.py** defines the site URL-to-view mappings. While this could contain _all_ the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
- **wsgi.py** is used to help your Django application communicate with the web server. You can treat this as boilerplate.
- **asgi.py** is a standard for Python asynchronous web apps and servers to communicate with each other. Asynchronous Server Gateway Interface (ASGI) is the asynchronous successor to Web Server Gateway Interface (WSGI). ASGI provides a standard for both asynchronous and synchronous Python apps, whereas WSGI provided a standard for synchronous apps only. ASGI is backward-compatible with WSGI and supports multiple servers and application frameworks.

## Creating the catalog application

Next, run the following command to create the _catalog_ application that will live inside our _locallibrary_ project. Make sure to run this command from the same folder as your project's **manage.py**:

```python
# Linux/macOS
python3 manage.py startapp catalog

# Windows
py manage.py startapp catalog
```

The tool creates a new folder and populates it with files for the different parts of the application (shown in the following example). Most of the files are named after their purpose (e.g. views should be stored in **views.py**, models in **models.py**, tests in **tests.py**, administration site configuration in **admin.py**, application registration in **apps.py**) and contain some minimal boilerplate code for working with the associated objects.

The updated project directory should now look like this:

```
locallibrary/
    manage.py
    locallibrary/
    catalog/
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        __init__.py
        migrations/
```

In addition we now have:
-   A _migrations_ folder, used to store "migrations" — files that allow you to _automatically update your database as you modify your models_.
-   **__init__.py** — an empty file created here so that Django/Python will recognize the folder as a [Python Package](https://docs.python.org/3/tutorial/modules.html#packages) and allow you to use its objects within other parts of the project.

>**Note:** Have you noticed what is missing from the files list above? While there is a place for your views and models, there is nowhere for you to put your URL mappings, templates, and static files. We'll show you how to create them further along (these aren't needed in every website but they are needed in this example).

## Registering the catalog application

Now that the application has been created, _we have to register it with the project_ so that it will be included when any tools are run (like adding models to the database for example). Applications are registered by adding them to the `INSTALLED_APPS` list in the project settings.

Open the project settings file, **django_projects/locallibrary/locallibrary/settings.py**, and find the definition for the `INSTALLED_APPS` list. Then add a new line at the end of the list, as shown below:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our new application
    'catalog.apps.CatalogConfig', #This object was created for us in /catalog/apps.py
]
```

The new line specifies the application configuration object (`CatalogConfig`) that was generated for you in **/locallibrary/catalog/apps.py** when you created the application.

> **Note:** You'll notice that there are already a lot of other `INSTALLED_APPS` (and `MIDDLEWARE`, further down in the settings file). These enable support for the [Django administration site](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site) and the functionality it uses (including sessions, authentication, etc.).

## Specifying the database

This is also the point where you would normally specify the database to be used for the project. It makes sense to use the same database for development and production where possible, in order to avoid minor differences in behavior. You can find out about the different options in [Databases](https://docs.djangoproject.com/en/4.0/ref/settings/#databases) (Django docs).

We'll use the SQLite database for this example, because we don't expect to require a lot of concurrent access on a demonstration database, and it requires no additional work to set up! You can see how this database is configured in **settings.py**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Note that sqlite3 is the default. 

## Other project settings

The **settings.py** file is also used for configuring a number of other settings, but at this point, you probably only want to change the [TIME_ZONE](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-TIME_ZONE) — this should be made equal to a string from the standard [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (the TZ column in the table contains the values you want). Change your `TIME_ZONE` value to one of these strings appropriate for your time zone, for example:

```python
TIME_ZONE = 'Europe/London'
```
There are two other settings you won't change now, but that you should be aware of:
- `SECRET_KEY`. This is a secret key that is used as part of Django's website security strategy. If you're not protecting this code in development, you'll need to use a different code (perhaps read from an environment variable or file) when putting it into production.
- `DEBUG`. This enables debugging logs to be displayed on error, rather than HTTP status code responses. This should be set to `False` in production as debug information is useful for attackers, but for now we can keep it set to `True`.

