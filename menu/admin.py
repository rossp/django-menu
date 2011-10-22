from django.contrib import admin
from menu.models import Menu, MenuItem

class MenuItemInline(admin.StackedInline):
    model = MenuItem

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]

admin.site.register(Menu, MenuAdmin)
