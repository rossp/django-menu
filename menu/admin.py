from django.contrib import admin
from menu.models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    ordering = ('order',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    inlines = [MenuItemInline,]


admin.site.register(Menu, MenuAdmin)
