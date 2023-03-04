from django.shortcuts import render
from .models import Event
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.utils import timezone
from datetime import date
from mysite.config import today_date, today_time
from django.contrib.auth import get_user_model
User = get_user_model()

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
    if request.method == "POST":
        if request.user in event.interested.all():
            event.interested.remove(request.user)
            request.user.events_interested.remove(event)
            messages.info(request, "You are no longer interested in this event")
        else:
            event.interested.add(request.user)
            request.user.events_interested.add(event)
            messages.success(request, "You are now interested in this event")
        return HttpResponseRedirect(request.path_info)
    manager, organizer = False, False
    if request.user == event.organizer or request.user.is_staff or request.user.is_superuser:
        manager = True
    if request.user == event.organizer:
        organizer = True
    
    curr_date = today_date if today_date else date.today()
    curr_time = today_time if today_time else timezone.now().time()

    print(curr_date, curr_time)

    event_started = False
    if event.start_date < curr_date or (event.start_date == curr_date and event.start_time < curr_time):
        event_started = True
    event_ended = False
    if event.end_date < curr_date or (event.end_date == curr_date and event.end_time < curr_time):
        event_ended = True
    
    return render(request, 'events/full_event.html', {'event': event, 'manager': manager, 'organizer': organizer, 'event_started': event_started, 'event_ended': event_ended})

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

# admit a single user to event
def admit_user(request, event_id, username):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    if not (request.user == event.organizer or request.user.is_staff or request.user.is_superuser):
        raise Http404("You are not the organizer of this event")
    try:
        user = User.objects.filter(username=username).first()
    except User.DoesNotExist:
        raise Http404(f"{user.username} does not exist")
    if user in event.interested.all() and user not in event.participants.all():
        event.participants.add(user)
        user.events_participated.add(event)
        messages.success(request, f"{user.username} has been admitted")
    elif user not in event.interested.all():
        messages.info(request, f"{user.username} is not interested in this event")
    else:
        messages.info(request, f"{user.username} is already admitted")
    event.save()
    user.save()
    return HttpResponseRedirect('../')

# propagate points
def propagate(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    if not (request.user == event.organizer or request.user.is_staff or request.user.is_superuser):
        raise Http404("You are not the organizer of this event")
    if event.points_propagated:
        raise Http404("Points have already been propagated")
    users = event.participants.all()
    print(users)
    for user in users:
        user.points_alltime += event.points
        user.points_quarterly += event.points
        user.coins += event.points
        user.save()
    event.points_propagated = True
    event.save()
    messages.success(request, "Points have been propagated")
    return HttpResponseRedirect('../')
