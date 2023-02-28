from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import CreateUserForm, EditProfileForm  # import custom user creation form
from events.models import Event
from django.utils import timezone
from datetime import date

# display home page
def index(request):
    events_list = Event.objects.order_by('-pub_date')
    upcoming_events = []
    upcoming_interested = []
    for event in events_list:
        if event.start_date >= date.today():
            if request.user.is_authenticated:
                if request.user in event.interested.all():
                    upcoming_interested.append(event)
            upcoming_events.append(event)
    upcoming_events = upcoming_events[:3]
    return render(request, 'home/index.html', {'upcoming_events': upcoming_events, 'upcoming_interested': upcoming_interested})

# display register page
def register(request):
    userForm = CreateUserForm()
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('/')
    return render(request, 'home/register.html', {'form': userForm})

# edit user profile
# update user profile
def update(request):
    if not request.user.is_authenticated:
        raise Http404("You are not logged in")
    editForm = EditProfileForm(instance=request.user)
    user = request.user
    if request.method == 'POST':
        editForm = EditProfileForm(request.POST, instance=request.user)
        if editForm.is_valid():
            editForm.save()
        return HttpResponseRedirect('/user/')

    return render(request, 'home/update.html', {'user': user, 'form': editForm})
