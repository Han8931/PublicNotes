# Overview

After we defined our models and created some initial library records to work with, it's time to write the code that presents that information to users. 
- The first thing we need to do is determine what information we want to display in our pages, 
- Also, we will define the URLs to use for returning those resources. 
- Then we'll create a URL mapper, views, and templates to display the pages.

The following diagram describes the main data flow, and the components required when handling HTTP requests and responses. As we already implemented the model, the main components we'll create are:

<img src="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page/basic-django.png", width=50%>
- URL mappers to forward the supported URLs (and any information encoded in the URLs) to the appropriate view functions.
- View functions to get the requested data from the models, create HTML pages that display the data, and return the pages to the user to view in the browser.
- Templates to use when rendering data in the views.

As this version of LocalLibrary is essentially read-only for end users, we just need to provide a landing page for the site (a home page), and pages that _display_ list and detail views for books and authors.

The URLs that we'll need for our pages are:
- `catalog/` — The home (index) page.
- `catalog/books/` — A list of all books.
- `catalog/authors/` — A list of all authors.
- `catalog/book/<id>` — The _detail view_ for a particular book, with a field primary key of `<id>` (the default). For example, the URL for the third book added to the list will be `/catalog/book/3`.
- `catalog/author/<id>` — The detail view for the specific author with a primary key field of `<id>`. For example, the URL for the 11th author added to the list will be `/catalog/author/11`.

The first three URLs will return the index page, books list, and authors list. These URLs do not encode any additional information, and the queries that fetch data from the database will always be the same. However, the results that the queries return will depend on the contents of the database.

By contrast the final two URLs will display detailed information about a specific book or author. These URLs encode the identity of the item to display (represented by `<id>` above). The URL mapper will extract the encoded information and pass it to the view, and the view will dynamically determine what information to get from the database. By encoding the information in the URL we will use a single set of a URL mapping, a view, and a template to handle all books (or authors).

> **Note:** With Django, you can construct your URLs however you require — you can encode information in the body of the URL as shown above, or include `GET` parameters in the URL, for example `/book/?id=6`. Whichever approach you use, the URLs should be kept clean, logical, and readable, as [recommended by the W3C](https://www.w3.org/Provider/Style/URI). The Django documentation recommends encoding information in the body of the URL to achieve better URL design.

As mentioned in the overview, the rest of this article describes how to construct the index page.

# Creating the index page

The first page we'll create is the index page (`catalog/`). The index page will include some static HTML, along with generated "counts" of different records in the database. To make this work we'll create a URL mapping, a view, and a template.

## URL mapping

When we created the skeleton website, we updated the **locallibrary/urls.py** file to ensure that whenever a URL that starts with `catalog/` is received, the _URLConf_ module `catalog.urls` will process the remaining substring.

The following code snippet from **locallibrary/urls.py** includes the `catalog.urls` module:

```python
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```

> **Note:** Whenever Django encounters the import function `django.urls.include()`, it splits the URL string at the designated end character and sends the remaining substring to the included _URLconf_ module for further processing.

We also created a placeholder file for the _URLConf_ module, named **/catalog/urls.py**. Add the following lines to that file:

```python
urlpatterns = [
    path('', views.index, name='index'),
]
```

The `path()` function defines the following:
- A URL pattern, which is an empty string: `''`. We'll discuss URL patterns in detail when working on the other views.
- A view function that will be called if the URL pattern is detected: `views.index`, which is the function named `index()` in the **views.py** file.

The `path()` function also specifies a `name` parameter, which is a unique identifier for _this_ particular URL mapping. You can use the name to "reverse" the mapper, i.e. to dynamically create a URL that points to the resource that the mapper is designed to handle. For example, we can use the name parameter to link to our home page from any other page by adding the following link in a template:

```python
<a href="{% url 'index' %}">Home</a>.
```

> **Note:** We can hard code the link as in `<a href="/catalog/">Home</a>`, but if we change the pattern for our home page, for example, to `/catalog/index` the templates will no longer link correctly. Using a reversed URL mapping is more robust.

## View (function-based)

A view is a function that processes an HTTP request, fetches the required data from the database, renders the data in an HTML page using an HTML template, and then returns the generated HTML in an HTTP response to display the page to the user. The index view follows this model — it fetches information about the number of `Book`, `BookInstance`, available `BookInstance` and `Author` records that we have in the database, and passes that information to a template for display.

Open **catalog/views.py** and note that the file already imports the `render()` shortcut function to generate an HTML file using a template and data:

```python
from django.shortcuts import render

# Create your views here.
```

Paste the following lines at the bottom of the file:

```python
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
```

The first line imports the model classes that we'll use to access data in all our views.

The first part of the view function fetches the number of records using the `objects.all()` attribute on the model classes. It also gets a list of `BookInstance` objects that have a value of 'a' (Available) in the status field. You can find more information about how to access model data in our previous tutorial Django Tutorial Part 3: Using models > Searching for records.

At the end of the view function we call the `render()` function to create an HTML page and return the page as a response. This shortcut function wraps a number of other functions to simplify a very common use case. The `render()` function accepts the following parameters:

- The original `request` object, which is an `HttpRequest`.
- An HTML template with placeholders for the data.
- A `context` variable, which is a Python dictionary, containing the data to insert into the placeholders.

We'll talk more about templates and the `context` variable in the next section. Let's get to creating our template so we can actually display something to the user!


# What does it look like?

At this point we have created all required resources to display the index page. Run the server (`python3 manage.py runserver`) and open `http://127.0.0.1:8000/` in your browser. 

<img src="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page/index_page_ok.png" width=70%>

