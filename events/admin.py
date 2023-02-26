from django.contrib import admin

from .models import Event, Tag, Prize

admin.site.site_header = '[Website] Admin'
admin.site.site_title = '[Website] Admin Areea'
admin.site.index_text = 'Welcome to the [Website] Admin'

admin.site.register(Event)
admin.site.register(Prize)
admin.site.register(Tag)
