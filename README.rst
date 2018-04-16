django-menu
-----------

BSD-licensed menu tools for Django, built by Ross Poulton <http://www.rossp.org>

django-menu provides a basic structure for you to build multiple navigation 
menus for your website, such as the header menubar. These menus can be easily 
maintained by staff using the Django administration without any knowledge 
of HTML or Django internals.

Sub-menus can also be easily built and displayed only for particular URIs.

Installation & Configuration:
-----------------------------

1. ``pip install django-menu``

2. Add ``menu`` to your ``INSTALLED_APPS``

3. ``./manage.py migrate menu`` (or ``./manage.py syncdb`` if you don't use South. You should use South.)

4. Add ``django.template.context_processors.request`` to your ``TEMPLATE`` settings. Below is a reasonably safe ``TEMPLATES`` setting for most small projects, however yours may vary.:

   .. code-block:: python
  
               TEMPLATES = [
                   {
                       'BACKEND': 'django.template.backends.django.DjangoTemplates',
                       'DIRS': [os.path.join(BASE_DIR, 'templates')],
                       'APP_DIRS': True,
                       'OPTIONS': {
                           'context_processors': [
                               'django.template.context_processors.debug',
                               'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages',
                               'django.template.context_processors.request',
                           ],
                       },
                   },
               ]

5. Add a Menu (eg called ``headernavigation``) and add some items to that menu

6. In your template, load the menu tags and embed your primary menu.

   .. code-block:: html+django

                <ul>{% load menubuilder %}{% menu headernavigation %}
                    {% for item in menuitems %}<li><a href="{{ item.url }}" title="{{ item.title|escape }}"{% if item.current %} class='current'{% endif %}>{{ item.title }}</a></li>
                    {% endfor %}
                </ul>


Submenus:
---------
If your template has a spot for navigation for the current sub-level of your 
website tree (i.e. a dozen pages underneath ``/about/``, plus a few under 
``/products/``)  you can create a new menu with a ``URI`` of ``/about/``.

In your template, instead of the ``{% menu %}`` tag use ``{% submenu %}``.  If a 
submenu for the current URI exists, it will be shown. The ``{{ submenu_items }}``
list contains your navigation items, ready to output like in the examples above.

Caching:
--------
To avoid hitting the database every time a user requests a page, the menu items are 
cached if you have a cache configured. Caching is not used when ``settings.DEBUG`` is ``True``.

To disable caching, set the setting ``MENU_CACHE_TIME`` to ``-1`` or remove your 
Django Cache configuration.

To enable caching to continue to let you make items available to anonymous or 
authenticated users, and to enable the "Current Page" functionality, the cache
will contain one dataset for each menu, authentication & path combination.
