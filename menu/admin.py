from django.contrib import admin
from menu.models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]

admin.site.register(Menu, MenuAdmin)
