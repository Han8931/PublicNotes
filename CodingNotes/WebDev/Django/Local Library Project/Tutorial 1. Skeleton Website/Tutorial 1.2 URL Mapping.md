# Hooking up the URL mapper (urlpatterns)

The website is created with a URL mapper file (**urls.py**) in the project folder. While you can use this file to manage all your URL mappings, it is more usual to defer mappings to the associated application. Open **locallibrary/locallibrary/urls.py** and note the instructional text which explains some of the ways to use the URL mapper.

```python
"""locallibrary URL Configuration

The `urlpatterns list` routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

The URL mappings are managed through the `urlpatterns` variable, which is a Python _list_ of `path()` functions. 
- Each `path()` function either associates a URL pattern to a _specific view_, which will be displayed when the pattern is matched, or with another list of URL pattern testing code (in this second case, the pattern becomes the "base URL" for patterns defined in the target module). 
- The `urlpatterns` list initially defines a single function that maps all URLs with the pattern _admin/_ to the module `admin.site.urls`, which contains the Administration application's own URL mapping definitions.

> **Note:** The route in `path()` is a string defining a URL pattern to match. This string might include a named variable (in angle brackets), e.g. `'catalog/<id>/'`. This pattern will match a URL like **catalog/_any_chars_/** and pass _`any_chars`_ to the view as a string with the parameter name `id`. We discuss path methods and route patterns further in later topics.

To add a new list item to the `urlpatterns` list, add the following lines to the bottom of the file. This new item includes a `path()` that forwards requests with the pattern `catalog/` to the module `catalog.urls` (the file with the relative URL **catalog/urls.py**).

```python
# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
```

Now let's redirect the **root URL** of our site (i.e. `127.0.0.1:8000`) to the URL `127.0.0.1:8000/catalog/`. This is the only app we'll be using in this project. To do this, we'll use a special view function, `RedirectView`, which takes the new relative URL to redirect to (`/catalog/`) as its first argument when the URL pattern specified in the `path()` function is matched (the root URL, in this case).

Add the following lines to the bottom of the file:

```python
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
```

Leave the first parameter of the path function empty to imply `'/'`. If you write the first parameter as `'/'` Django will give you the following warning when you start the development server:

```
System check identified some issues:

WARNINGS:
?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'.
Remove this slash as it is unnecessary.
If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
```

Django does not serve static files like CSS, JavaScript, and images by default, but it can be useful for the development web server to do so while you're creating your site. As a final addition to this URL mapper, you can enable the serving of static files during development by appending the following lines.

Add the following final block to the bottom of the file now:
```python
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

>**Note:** There are a number of ways to extend the `urlpatterns` list (previously, we just appended a new list item using the `+=` operator to clearly separate the old and new code). We could have instead just included this new pattern-map in the original list definition:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

As a final step, create a file inside your catalog folder called **urls.py**, and add the following text to define the (empty) imported `urlpatterns`. This is where we'll add our patterns as we build the application.

```python
from django.urls import path
from . import views

urlpatterns = [

]
```

