from django.shortcuts import render
from .models import Event
from django.http import HttpResponse, Http404

# display events
def events(request):
    events_list = Event.objects.order_by('-pub_date')
    content = {'events_list': events_list}
    return render(request, 'events/events.html', content)

# display event details
def full_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/full_event.html', {'event': event})
