---
tags: web, django, python
---
# Introduction to Django

Django web applications typically group the code that handles each of these steps into separate files:
<img src="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png" alt="Han", title="This is Han", width=40%>
-   **URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.
-   **View:** A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via _models_, and delegate the formatting of the response to _templates_.
-   **Models:** Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database.
-   **Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A _view_ can dynamically create an HTML page using an HTML template, populating it with data from a _model_. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

>**Note:** Django refers to this organization as the "__Model View Template (MVT)" architecture. It has many similarities to the more familiar [Model View Controller](https://developer.mozilla.org/en-US/docs/Glossary/MVC) architecture.

## Model View Controller

<img src="https://developer.mozilla.org/en-US/docs/Glossary/MVC/model-view-controller-light-blue.png", width=40%>
### 1. The Model
_The model defines what data the app should contain_. If the state of this data changes, then the model will usually notify the view (so the display can change as needed) and sometimes the controller (if different logic is needed to control the updated view). Going back to our shopping list app, the model would specify what data the list items should contain — item, price, etc. — and what list items are already present.

### 2. The View
_The view defines how the app's data should be displayed_. In our shopping list app, the view would define how the list is presented to the user, and receive the data to display from the model.

### 3. The Controller
_The controller contains logic that updates the model and/or view in response to input from the users of the app_. So for example, our shopping list could have input forms and buttons that allow us to add or delete items. These actions require the model to be updated, so the input is sent to the controller, which then manipulates the model as appropriate, which then sends updated data to the view.

You might however also want to just update the view to display the data in a different format, e.g., change the item order to alphabetical, or lowest to highest price. In this case the controller could handle this directly without needing to update the model.

## Model View Template
Django only loosely follows the traditional MVC approach with its own version often called Model-View-Template (MVT).

- Model: Manages data and core business logic
- View: Describes which data is sent to the user but not its presentation
- Template: Presents the data as HTML with optional CSS, JavaScript, and Static Assets
- URL Configuration: Regular-expression components configured to a View

### Django response/request cycle:
- HTTP Request -> URL -> View -> Model and Template -> HTTP Response

# Sending the request to the right view (urls.py)

A URL mapper is typically stored in a file named **urls.py**. In the example below, the mapper (`urlpatterns`) defines a list of mappings between _routes_ (specific URL _patterns)_ and corresponding view functions. If an HTTP Request is received that has a URL matching a specified pattern, then the associated view function will be called and passed the request.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('catalog/', include('catalog.urls')),
    re_path(r'^([0-9]+)/$', views.best),
]
```
The first argument to both methods is a route (pattern) that will be matched. The `path()` method uses angle brackets to define parts of a URL that will be captured and passed through to the view function as named arguments. The `re_path()` function uses a regular expression

The second argument is another function that will be called when the pattern is matched. The notation `views.book_detail` indicates that the function is called `book_detail()` and can be found in a module called `views` (i.e. inside a file named `views.py`)

# Handling the request (views.py)

Views are the heart of the web application, receiving HTTP requests from web clients and returning HTTP responses. In between, they marshal the other resources of the framework to access databases, render templates, etc.

The example below shows a minimal view function `index()`, which could have been called by our URL mapper in the previous section. Like all view functions it receives an `HttpRequest` object as a parameter (`request`) and returns an `HttpResponse` object. In this case we don't do anything with the request, and our response returns a hard-coded string. We'll show you a request that does something more interesting in a later section.

```python
# filename: views.py (Django view functions)

from django.http import HttpResponse

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    return HttpResponse('Hello from Django!')
```

# Defining data models (models.py)

Django web applications manage and query data through Python objects referred to as models. Models define the structure of stored data, including the field _types_ and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. The definition of the model is independent of the underlying database — you can choose one of several as part of your project settings. Once you've chosen what database you want to use, you don't need to talk to it directly at all — you just write your model structure and other code, and Django handles all the "dirty work" of communicating with the database for you.

The code snippet below shows a very simple Django model for a `Team` object. The `Team` class is derived from the Django class `models.Model`. It defines the team name and team level as character fields and specifies a maximum number of characters to be stored for each record. The `team_level` can be one of several values, so we define it as a choice field and provide a mapping between choices to be displayed and data to be stored, along with a default value.

```python
# filename: models.py

from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=40)

    TEAM_LEVELS = (
        ('U09', 'Under 09s'),
        ('U10', 'Under 10s'),
        ('U11', 'Under 11s'),
        # …
        # list other team levels
    )
    team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')
```

# Querying data (views.py)

The Django model provides a simple query API for searching the associated database. This can match against a number of fields at a time using different criteria (e.g. exact, case-insensitive, greater than, etc.), and can support complex statements (for example, you can specify a search on U11 teams that have a team name that starts with "Fr" or ends with "al").

The code snippet shows a view function (resource handler) for displaying all of our U09 teams. The `list_teams = Team.objects.filter(team_level__exact="U09")` line shows how we can use the model query API to filter for all records where the `team_level` field has exactly the text '`U09`' (note how this criteria is passed to the `filter()` function as an argument, with the field name and match type separated by a double underscore: **`team_level__exact`**).

```python
## filename: views.py

from django.shortcuts import render
from .models import Team

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context)
```

This function uses the `render()` function to create the `HttpResponse` that is sent back to the browser. This function is a _shortcut_; it creates an HTML file by combining a specified HTML template and some data to insert in the template (provided in the variable named "`context`"). In the next section we show how the template has the data inserted in it to create the HTML.

# Rendering data (HTML templates)

_Template systems allow you to specify the structure of an output document_, using placeholders for data that will be filled in when a page is generated. Templates are often used to create HTML, but can also create other types of document. Django supports both its native templating system and another popular Python library called Jinja2 out of the box (it can also be made to support other systems if needed).

The code snippet shows what the HTML template called by the `render()` function in the previous section might look like. This template has been written under the assumption that it will have access to a list variable called `youngest_teams` when it is rendered (this is contained in the `context` variable inside the `render()` function above). Inside the HTML skeleton we have an expression that first checks if the `youngest_teams` variable exists, and then iterates it in a `for` loop. On each iteration the template displays each team's `team_name` value in an ``[`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)`` element.

```html
## filename: best/templates/best/index.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Home page</title>
</head>
<body>
  {% if youngest_teams %}
    <ul>
      {% for team in youngest_teams %}
        <li>{{ team.team_name }}</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No teams are available.</p>
  {% endif %}
</body>
</html>
```

# Web Server vs Web Application Server
- Web server needs to prepare all html forms to create a web site, which is often called static.
- On the other hand web application server is dynamically creating pages. 
	- Typically hard to study and slower than web server based web site. 
	- Advantages in maintenance. 
	- Highly customizable for users. 


