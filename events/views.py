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
            request.user.events_interested.remove(event)
            messages.info(request, "You are no longer interested in this event")
        else:
            event.interested.add(request.user)
            request.user.events_interested.add(event)
            messages.success(request, "You are now interested in this event")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'events/full_event.html', {'event': event})

# admit users to event
def admit(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    if not (request.user == event.organizer or request.user.is_staff or request.user.is_superuser):
        raise Http404("You are not the organizer of this event")
    
    users = event.interested.all().order_by('-last_name')
    if request.method == "POST":
        checked_users = request.POST.getlist('admit')
        for user in users:
            if user.username in checked_users and user not in event.participants.all():
                event.participants.add(user)
                user.events_participated.add(event)
            elif user.username not in checked_users and user in event.participants.all():
                event.participants.remove(user)
                user.events_participated.remove(event)
        messages.success(request, "Attendance has been updated")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'events/admit.html', {'event': event, 'users': users})
