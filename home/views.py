from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import CreateUserForm, EditProfileForm  # import custom user creation form
from events.models import Event
from django.utils import timezone
from datetime import date
from mysite.config import today_date, today_time
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
import random
from prizes.models import Prize

# display home page
def index(request):
    # upcoming and upcoming interseted events
    events_list = Event.objects.order_by('-pub_date')
    upcoming_events = []
    upcoming_interested = []
    curr_date = today_date if today_date else date.today()
    curr_time = today_time if today_time else timezone.now().time()
    for event in events_list:
        if curr_date <= event.start_date or (curr_date == event.start_date and curr_time <= event.start_time):
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

# end quarter, reset points, distribute prizes
def end_quarter(request):
    if not request.user.is_authenticated:
        raise Http404("You are not logged in")
    if not request.user.is_superuser:
        raise Http404('You are not an admin!')
    users = User.objects.all().order_by('-points_quarterly')
    winners = [users[0]]
    for grade in range(9, 13):
        grade_users = [user for user in users if user.grade == grade]
        if grade_users:
            winners.append(random.choice(grade_users))
    print(winners)

    for user in users:
        if user in winners:
            if user.prizes_redeemed.count() == Prize.objects.count():
                user.delayed_notification = 'The quarter has ended. You won a $10 gift card because you have redeemed all the prizes!'
            else:
                while True:
                    prize = random.choice(Prize.objects.all())
                    if prize not in user.prizes_redeemed.all():
                        user.delayed_notification = f'The quarter has ended. You won a {prize.prize_name}!'
                        user.prizes_redeemed.add(prize)
                        break
        else:
            user.delayed_notification = 'The quarter has ended!'
        user.points_quarterly = 0
        user.save()
    messages.success(request, 'Quarterly points reset and prizes distributed!')
    return HttpResponseRedirect('../')
