from django.contrib import admin

from .models import Event, Tag, Prize

admin.site.site_header = '[Website] Admin'
admin.site.site_title = '[Website] Admin Areea'
admin.site.index_text = 'Welcome to the [Website] Admin'

class TagInline(admin.TabularInline):
    model = Tag
    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_title', 'organizer', 'description', 'location', 'image']}),
        ('Date information', {'fields': ['start_date', 'start_time', 'end_date', 'end_time']}),
        ('Points', {'fields': ['points']}),
        ('Visibility', {'fields': ['visibility']}),
    ]
    inlines = [TagInline]
    list_display = ('event_title', 'organizer', 'start_date', 'end_date', 'points', 'visibility')
    list_filter = ['start_date', 'end_date']
    search_fields = ['event_title', 'organizer']

admin.site.register(Event, EventAdmin)
admin.site.register(Prize)

