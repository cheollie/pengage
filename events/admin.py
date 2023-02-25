from django.contrib import admin

from .models import Event, Prize

admin.site.register(Event)
admin.site.register(Prize)