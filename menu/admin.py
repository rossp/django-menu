from django.contrib import admin
from menu.models import Menu, MenuItem

admin.site.register([Menu, MenuItem])
