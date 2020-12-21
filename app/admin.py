from django.contrib import admin

from .models import Menu, MenuGroup, Posts

admin.site.register(Menu)
admin.site.register(Posts)
admin.site.register(MenuGroup)
