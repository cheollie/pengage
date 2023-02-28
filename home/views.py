from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import CreateUserForm, EditProfileForm  # import custom user creation form
from events.models import Event
from django.utils import timezone
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

# display home page
def index(request):
    # upcoming and upcoming interseted events
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

    is_logged_in = request.user.is_authenticated

    # quarterly leaderboard
    quarterly_leaderboard = User.objects.order_by('-points_quarterly')
    if not is_logged_in or list(quarterly_leaderboard).index(request.user) < 5:
        quarterly_leaderboard = quarterly_leaderboard[:5]
    else:
        ind = list(quarterly_leaderboard).index(request.user)
        quarterly_leaderboard = quarterly_leaderboard[:2] + quarterly_leaderboard[ind-1:ind+2]
    
    # all time leaderboard
    alltime_leaderboard = User.objects.order_by('-points_alltime')
    if not is_logged_in or list(alltime_leaderboard).index(request.user) < 5:
        alltime_leaderboard = alltime_leaderboard[:5]
    else:
        ind = list(alltime_leaderboard).index(request.user)
        alltime_leaderboard = alltime_leaderboard[:2] + alltime_leaderboard[ind-1:ind+2]


    return render(request, 'home/index.html', {'upcoming_events': upcoming_events, 'upcoming_interested': upcoming_interested, 'quarterly_leaderboard': quarterly_leaderboard, 'alltime_leaderboard': alltime_leaderboard})

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
