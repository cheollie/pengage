from django.shortcuts import render
from .models import Event
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages

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
    print(request)
    if request.method == "POST":
        print(request.user)
        if request.user in event.interested.all():
            event.interested.remove(request.user)
            messages.info(request, "You are no longer interested in this event")
        else:
            event.interested.add(request.user)
            messages.success(request, "You are now interested in this event")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'events/full_event.html', {'event': event})
