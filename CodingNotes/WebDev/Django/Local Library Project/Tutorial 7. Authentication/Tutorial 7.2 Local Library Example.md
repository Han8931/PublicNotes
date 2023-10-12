# Listing the current user's books

Now that we know how to restrict a page to a particular user, let's create a view of the books that the current user has borrowed.

Unfortunately, we don't yet have any way for users to borrow books! So before we can create the book list we'll first extend the `BookInstance` model to support the concept of borrowing and use the Django Admin application to loan a number of books to our test user.

## Models

First, we're going to have to make it possible for users to have a `BookInstance` on loan (we already have a `status` and a `due_back` date, but we don't yet have any association between this model and a User. We'll create one using a `ForeignKey` (one-to-many) field. We also need an easy mechanism to test whether a loaned book is overdue.

Open **catalog/models.py**, and import the `User` model from `django.contrib.auth.models` (add this just below the previous import line at the top of the file, so `User` is available to subsequent code that makes use of it):

```python
from django.contrib.auth.models import User
```

Next, add the `borrower` field to the `BookInstance` model:

```python
borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
```

While we're here, let's add a property that we can call from our templates to tell if a particular book instance is overdue. While we could calculate this in the template itself, using a [property](https://docs.python.org/3/library/functions.html#property) as shown below will be much more efficient.

Add this somewhere near the top of the file:

```python
from datetime import date
```

Now add the following property definition to the `BookInstance` class:

>**Note:** The following code uses Python's `bool()` function, which evaluates an object or the resulting object of an expression, and returns `True` unless the result is "falsy", in which case it returns `False`. In Python an object is _falsy_ (evaluates as `False`) if it is: empty (like `[]`, `()`, `{}`), `0`, `None` or if it is `False`.

```python
@property
def is_overdue(self):
    """Determines if the book is overdue based on due date and current date."""
    return bool(self.due_back and date.today() > self.due_back)
```

>**Note:** We first verify whether `due_back` is empty before making a comparison. An empty `due_back` field would cause Django to throw an error instead of showing the page: empty values are not comparable. This is not something we would want our users to experience!

Now that we've updated our models, we'll need to make fresh migrations on the project and then apply those migrations:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

## Admin

Now open **catalog/admin.py**, and add the `borrower` field to the `BookInstanceAdmin` class in both the `list_display` and the `fieldsets` as shown below. This will make the field visible in the Admin section, allowing us to assign a `User` to a `BookInstance` when needed.

```python
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
```

## Loan a few books

Now that it's possible to loan books to a specific user, go and loan out a number of `BookInstance` records. Set their `borrowed` field to your test user, make the `status` "On loan", and set due dates both in the future and the past.

>**Note:** We won't spell the process out, as you already know how to use the Admin site!

## On loan view

Now we'll add a view for getting the list of all books that have been loaned to the current user. We'll use the same generic class-based list view we're familiar with, but this time we'll also import and derive from `LoginRequiredMixin`, so that _only a logged in user can call this view_. We will also choose to declare a `template_name`, rather than using the default, because we may end up having a few different lists of BookInstance records, with different views and templates.

Add the following to `catalog/views.py`:

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
```

In order to restrict our query to just the `BookInstance` objects for the current user, we re-implement `get_queryset()` as shown above. Note that "o" is the stored code for "on loan" and we order by the `due_back` date so that the oldest items are displayed first.

## URL conf for on loan books

Now open **/catalog/urls.py** and add a `path()` pointing to the above view (you can just copy the text below to the end of the file).

```python
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
```

## Template for on-loan books

Now, all we need to do for this page is add a template. First, create the template file **/catalog/templates/catalog/bookinstance_list_borrowed_user.html** and give it the following contents:

```django
{% extends "base_generic.html" %}

{% block content %}
    <h1>Borrowed books</h1>

    {% if bookinstance_list %}
    <ul>

      {% for bookinst in bookinstance_list %}
      <li class="{% if bookinst.is_overdue %}text-danger{% endif %}">
        <a href="{% url 'book-detail' bookinst.book.pk %}">{{ bookinst.book.title }}</a> ({{ bookinst.due_back }})
      </li>
      {% endfor %}
    </ul>

    {% else %}
      <p>There are no books borrowed.</p>
    {% endif %}
{% endblock %}
```

This template is very similar to those we've created previously for the `Book` and `Author` objects. The only "new" thing here is that we check the method we added in the model `(bookinst.is_overdue`) and use it to change the color of overdue items.

When the development server is running, you should now be able to view the list for a logged in user in your browser at `http://127.0.0.1:8000/catalog/mybooks/`. Try this out with your user logged in and logged out (in the second case, you should be redirected to the login page).

## Add the list to the sidebar

The very last step is to add a link for this new page into the sidebar. We'll put this in the same section where we display other information for the logged in user.

Open the base template (**/locallibrary/catalog/templates/base_generic.html**) and add the "My Borrowed" line to the sidebar in the position shown below.

```django
 <ul class="sidebar-nav">
   {% if user.is_authenticated %}
   <li>User: {{ user.get_username }}</li>

   <li><a href="{% url 'my-borrowed' %}">My Borrowed</a></li>

   <li><a href="{% url 'logout' %}?next={{ request.path }}">Logout</a></li>
   {% else %}
   <li><a href="{% url 'login' %}?next={{ request.path }}">Login</a></li>
   {% endif %}
 </ul>
```

## What does it look like?

When any user is logged in, they'll see the _My Borrowed_ link in the sidebar, and the list of books displayed as below (the first book has no due date, which is a bug we hope to fix in a later tutorial!).

![Library - borrowed books by user](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication/library_borrowed_by_user.png)

# Permissions

Permissions are associated with models and define the operations that can be performed on a model instance by a user who has the permission. By default, Django automatically gives _add_, _change_, and _delete_ permissions to all models, which allow users with the permissions to perform the associated actions via the admin site. You can define your own permissions to models and grant them to specific users. You can also change the permissions associated with different instances of the same model.

Testing on permissions in views and templates is then very similar to testing on the authentication status (and in fact, testing for a permission also tests for authentication).

## Models

Defining permissions is done on the model "`class Meta`" section, using the `permissions` field. 
- You can specify as many permissions as you need in a tuple, each permission itself being defined in a nested tuple containing the permission name and permission display value. 
- For example, we might define a permission to allow a user to mark that a book has been returned as shown:

```python
class BookInstance(models.Model):
    # …
    class Meta:
        # …
        permissions = (("can_mark_returned", "Set book as returned"),)
```

We could then assign the permission to a "Librarian" group in the Admin site.

Open the **catalog/models.py**, and add the permission as shown above. You will need to re-run your migrations (call `python3 manage.py makemigrations` and `python3 manage.py migrate`) to update the database appropriately.

## Templates

The current user's permissions are stored in a template variable called `{{ perms }}`. 
- You can check whether the current user has a particular permission using the specific variable name within the associated Django "app" — e.g. `{{ perms.catalog.can_mark_returned }}` will be `True` if the user has this permission, and `False` otherwise. 
- We typically test for the permission using the template `{% if %}` tag as shown:

```django
{% if perms.catalog.can_mark_returned %}
    <!-- We can mark a BookInstance as returned. -->
    <!-- Perhaps add code to link to a "book return" view here. -->
{% endif %}
```

## Views

Permissions can be tested: 
- In function view using the `permission_required` decorator
- In a class-based view using the `PermissionRequiredMixin`. 

The pattern are the same as for login authentication, though of course, you might reasonably have to add multiple permissions.

Function view decorator:
```python
from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
@permission_required('catalog.can_edit')
def my_view(request):
    # …
```

A permission-required mixin for class-based views.
```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_mark_returned'
    # Or multiple permissions
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    # Note that 'catalog.can_edit' is just an example
    # the catalog application doesn't have such permission!
```

>**Note:** There is a small default difference in the behavior above. By **default** for a logged-in user with a permission violation:

- `@permission_required` redirects to login screen (HTTP Status 302).
- `PermissionRequiredMixin` returns 403 (HTTP Status Forbidden).

Normally you will want the `PermissionRequiredMixin` behavior: return 403 if a user is logged in but does not have the correct permission. To do this for a function view use `@login_required` and `@permission_required` with `raise_exception=True` as shown:
```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def my_view(request):
    # …
```

## Example

We won't update the _LocalLibrary_ here; perhaps in the next tutorial!