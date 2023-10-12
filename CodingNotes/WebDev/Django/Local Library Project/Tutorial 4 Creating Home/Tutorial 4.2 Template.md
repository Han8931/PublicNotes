The official Django website provides a guide for template with details [reference](https://docs.djangoproject.com/en/4.2/topics/templates/)
# Overview

_A template is a text file that defines the structure or layout of a file (such as an HTML page)_, it uses placeholders to represent actual content.

A Django application created using **startapp** (like the skeleton of this example) will look for templates in a subdirectory named '**templates**' of your applications. For example, in the index view that we just added, the `render()` function will expect to find the file **_index.html_** in **/locallibrary/catalog/templates/** and will raise an error if the file is not present.

You can check this by saving the previous changes and accessing `127.0.0.1:8000` in your browser - it will display a fairly intuitive error message: "`TemplateDoesNotExist at /catalog/`", and other details.

> **Note:** Based on your project's settings file, Django will look for templates in a number of places, searching in your installed applications by default. You can find out more about how Django finds templates and what template formats it supports in [the Templates section of the Django documentation](https://docs.djangoproject.com/en/4.0/topics/templates/).

# Extending templates

The index template will need standard HTML markup for the head and body, along with navigation sections to link to the other pages of the site (which we haven't created yet), and to sections that display introductory text and book data.

Much of the HTML and navigation structure will be the same in every page of our site. Instead of duplicating boilerplate code on every page, _you can use the Django template language to declare a base template, and then extend it to replace just the bits that are different for each specific page_.

The following code snippet is a _sample_ base template from a **base_generic.html** file. We'll be creating the template for LocalLibrary shortly. The sample below includes common HTML with sections for a title, a sidebar, and main contents marked with the named `block` and `endblock` _template tags_. You can leave the blocks empty, or include default content to use when rendering pages derived from the template.

> **Note:**  Template tags are functions that you can use in a template to loop through lists, perform conditional operations based on the value of a variable, and so on. In addition to template tags, the template syntax allows you to reference variables that are passed into the template from the view, and use _template filters_ to format variables (for example, to convert a string to lower case).

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    {% block title %}
      <title>Local Library</title>
    {% endblock %}
  </head>
  <body>
    {% block sidebar %}
      <!-- insert default navigation text for every page -->
    {% endblock %}
    {% block content %}
      <!-- default content text (typically empty) -->
    {% endblock %}
  </body>
</html>
```

When defining a template for a particular view, we first specify the base template using the `extends` template tag — see the code sample below. Then, we declare what sections from the template we want to replace (if any), using `block`/`endblock` sections as in the base template.

For example, the code snippet below shows how to use the `extends` template tag and override the `content` block. The generated HTML will include the code and structure defined in the base template, including the default content you defined in the `title` block, but the new `content` block in place of the default one.

```html
{% extends "base_generic.html" %}

{% block content %}
  <h1>Local Library Home</h1>
  <p>
    Welcome to LocalLibrary, a website developed by
    <em>Mozilla Developer Network</em>!
  </p>
{% endblock %}
```

# The LocalLibrary base template

We will use the following code snippet as the base template for the _LocalLibrary_ website. As you can see, it contains some HTML code and defines blocks for `title`, `sidebar`, and `content`. We have a default title and a default sidebar with links to lists of all books and authors, both enclosed in blocks to be easily changed in the future.

>**Note:** We also introduce two additional template tags: `url` and `load static`. These tags will be explained in following sections.

Create a new file **base_generic.html** in **/locallibrary/catalog/templates/** and paste the following code to the file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    {% block title %}
      <title>Local Library</title>
    {% endblock %}
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous" />
    <!-- Add additional CSS in static file -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-2">
          {% block sidebar %}
            <ul class="sidebar-nav">
              <li><a href="{% url 'index' %}">Home</a></li>
              <li><a href="">All books</a></li>
              <li><a href="">All authors</a></li>
            </ul>
          {% endblock %}
        </div>
        <div class="col-sm-10 ">{% block content %}{% endblock %}</div>
      </div>
    </div>
  </body>
</html>
```

The template includes CSS from [Bootstrap](https://getbootstrap.com/) to improve the layout and presentation of the HTML page. Using Bootstrap (or another client-side web framework) is a quick way to create an attractive page that displays well on different screen sizes.

The base template also references a local CSS file (**styles.css**) that provides additional styling. Create a **styles.css** file in **/locallibrary/catalog/static/css/** and paste the following code in the file:

```python
.sidebar-nav {
  margin-top: 20px;
  padding: 0;
  list-style: none;
}
```

## The index template

Create a new HTML file **index.html** in **/locallibrary/catalog/templates/** and paste the following code in the file. This code extends our base template on the first line, and then replaces the default `content` block for the template.

```html
{% extends "base_generic.html" %}

{% block content %}
  <h1>Local Library Home</h1>
  <p>
    Welcome to LocalLibrary, a website developed by
    <em>Mozilla Developer Network</em>!
  </p>
  <h2>Dynamic content</h2>
  <p>The library has the following record counts:</p>
  <ul>
    <li><strong>Books:</strong> {{ num_books }}</li>
    <li><strong>Copies:</strong> {{ num_instances }}</li>
    <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
    <li><strong>Authors:</strong> {{ num_authors }}</li>
  </ul>
{% endblock %}
```

In the _Dynamic content_ section we declare placeholders (_template variables_) for the information from the view that we want to include. The variables are enclosed with double brace (handlebars).

>**Note:** You can easily recognize template variables and template tags (functions) - variables are enclosed in double braces (`{{ num_books }}`), and tags are enclosed in single braces with percentage signs (`{% extends "base_generic.html" %}`).

The important thing to note here is that variables are named with the _keys_ that we pass into the `context` dictionary in the `render()` function of our view (see sample below). Variables will be replaced with their associated _values_ when the template is rendered.

```python
context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
}

return render(request, 'index.html', context=context)
```

## Referencing static files in templates

Your project is likely to use static resources, including JavaScript, CSS, and images. Because the location of these files might not be known (or might change), Django allows you to specify the location in your templates relative to the `STATIC_URL` global setting. The default skeleton website sets the value of `STATIC_URL` to '`/static/`', but you might choose to host these on a content delivery network or elsewhere.

Within the template you first call the `load` template tag specifying "static" to add the template library, as shown in the code sample below. You can then use the `static` template tag and specify the relative URL to the required file.

```html
<!-- Add additional CSS in static file -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}" />
```

You can add an image into the page in a similar way, for example:

```html
{% load static %}
<img
  src="{% static 'catalog/images/local_library_model_uml.png' %}"
  alt="UML diagram"
  style="width:555px;height:540px;" />
```

>**Note:** The samples above specify where the files are located, but Django does not serve them by default. We configured the development web server to serve files by modifying the global URL mapper (**/locallibrary/locallibrary/urls.py**) when we [created the website skeleton](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website), but still need to enable file serving in production. We'll look at this later.

For more information on working with static files see [Managing static files](https://docs.djangoproject.com/en/4.0/howto/static-files/) in the Django documentation.

## Linking to URLs

The base template above introduced the `url` template tag.

```html
<li><a href="{% url 'index' %}">Home</a></li>
```

This tag accepts the name of a `path()` function called in your **urls.py** and the values for any arguments that the associated view will receive from that function, and returns a URL that you can use to link to the resource.

## Configuring where to find the templates

The location where Django searches for templates is specified in the `TEMPLATES` object in the **settings.py** file. The default **settings.py** (as created for this tutorial) looks something like this:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

The setting of `'APP_DIRS': True`, is the most important, as _it tells Django to search for templates in a subdirectory of each application in the project, named "templates"_ (this makes it easier to group templates with their associated application for easy re-use).

We can also specify specific locations for Django to search for directories using `'DIRS': []` (but that isn't needed yet).

>**Note:** You can find out more about how Django finds templates and what template formats it supports in [the Templates section of the Django documentation](https://docs.djangoproject.com/en/4.0/topics/templates/).

