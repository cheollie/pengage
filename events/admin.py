from django.contrib import admin

from .models import Event, Tag

admin.site.site_header = '[Website] Admin'
admin.site.site_title = '[Website] Admin Area'
admin.site.index_text = 'Welcome to the [Website] Admin'

admin.site.register(Event)
admin.site.register(Tag)
