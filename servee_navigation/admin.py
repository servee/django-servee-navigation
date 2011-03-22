from treebeard.admin import TreeAdmin
from servee_navigation.models import MenuItem
from django.contrib import admin


class MenuItemAdmin(TreeAdmin):
    list_display = (
        'title', 'urlpath',
        )

admin.site.register(MenuItem, MenuItemAdmin)
