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

1. `pip install django-menu`

2. Add `menu` to your `INSTALLED_APPS`

3. Add `django.core.context_processors.request` to your `TEMPLATE_CONTEXT_PROCESSORS`. It is not there by defult. The defualt `TEMPLATE_CONTEXT_PROCESSORS` are `"django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages"`

4. Add a Menu (eg called `headernavigation`) and add some items to that menu

5. In your template, load the menu tags and embed your primary menu.:::

                <ul>{% load menubuilder %}{% menu headernavigation %}
                    {% for item in menuitems %}<li><a href="{{ item.url }}" title="{{ item.title|escape }}"{% if item.current %} class='current'{% endif %}>{{ item.title }}</a></li>
                    {% endfor %}
                </ul>


Submenus:
---------
If your template has a spot for navigation for the current sub-level of your 
website tree (i.e. a dozen pages underneath `/about/`, plus a few under 
`/products/`)  you can create a new menu with a `URI` of `/about/`.

In your template, instead of the `{% menu %}` tag use `{% submenu %}`.  If a 
submenu for the current URI exists, it will be shown. The `{{ submenu_items }}`
list contains your navigation items, ready to output like in the examples above.
