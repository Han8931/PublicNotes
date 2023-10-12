## Testing the website framework

At this point we have a complete skeleton project. The website doesn't actually do anything yet, but it's worth running it to make sure that none of our changes have broken anything. Before we do that, we should first run a _database migration_. This updates our database (to include any models in our installed applications) and removes some build warnings.

### Running database migrations

Django uses an Object-Relational-Mapper (ORM) to map model definitions in the Django code to the data structure used by the underlying database. As we change our model definitions, Django tracks the changes and can create database migration scripts (in **/locallibrary/catalog/migrations/**) to automatically migrate the underlying data structure in the database to match the model.

When we created the website, Django automatically added a number of models for use by the admin section of the site (which we'll look at later). Run the following commands to define tables for those models in the database (make sure you are in the directory that contains **manage.py**):

```
python3 manage.py makemigrations
python3 manage.py migrate
```

> **Warning:** You'll need to run these commands every time your models change in a way that will affect the structure of the data that needs to be stored (including both addition and removal of whole models and individual fields).

- The `makemigrations` command _creates_ (but does not apply) the migrations for all applications installed in your project. You can specify the application name as well to just run a migration for a single app. This gives you a chance to check out the code for these migrations before they are applied. If you're a Django expert, you may choose to tweak them slightly!
- The `migrate` command is what applies the migrations to your database. Django tracks which ones have been added to the current database.

## Running the website

During development, you can serve the website first using the _development web server_, and then viewing it on your local web browser.

>**Note:** The development web server is not robust or performant enough for production use, but it is a very easy way to get your Django website up and running during development to give it a convenient quick test. By default it will serve the site to your local computer (`http://127.0.0.1:8000/)`, but you can also specify other computers on your network to serve to. For more information see [django-admin and manage.py: runserver](https://docs.djangoproject.com/en/4.0/ref/django-admin/#runserver) (Django docs).

Run the _development web server_ by calling the `runserver` command (in the same directory as **manage.py**):

```python
$ python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 01, 2022 - 04:08:45
Django version 4.0.2, using settings 'locallibrary.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Once the server is running, you can view the site by navigating to `http://127.0.0.1:8000/` in your local web browser. You should see a site error page.  This error page is expected because we don't have any pages/urls defined in the `catalog.urls` module (which we're redirected to when we get a URL to the root of the site).

>**Note:** The example page demonstrates a great Django feature — automated debug logging. Whenever a page cannot be found, Django displays an error screen with useful information or any error raised by the code. In this case, we can see that the URL we've supplied doesn't match any of our URL patterns (as listed). Logging is turned off in production (which is when we put the site live on the Web), in which case a less informative but more user-friendly page will be served.