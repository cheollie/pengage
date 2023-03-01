from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, Http404
User = get_user_model()
from django.contrib import messages


# display user profile
def user(request, username=None):
    if username == None and request.user.is_authenticated:
        return HttpResponseRedirect('/user/' + request.user.username)
    elif username == None:
        raise Http404("You are not logged in")
    user = User.objects.filter(username=username).first()
    if user == None:
        raise Http404("User does not exist")
    
    # get rank
    quarterly_overall = list(User.objects.order_by('-points_quarterly')).index(user) + 1
    quarterly_grade = list(User.objects.filter(grade=user.grade).order_by('-points_quarterly')).index(user) + 1
    alltime_overall = list(User.objects.order_by('-points_alltime')).index(user) + 1
    alltime_grade = list(User.objects.filter(grade=user.grade).order_by('-points_alltime')).index(user) + 1

    # if delayed notification, display it
    if user.delayed_notification != '':
        messages.success(request, user.delayed_notification)
        user.delayed_notification = ''
        user.save()

    content = {'user': user, 'is_self': request.user == user, 'quarterly_overall': quarterly_overall, 'quarterly_grade': quarterly_grade, 'alltime_overall': alltime_overall, 'alltime_grade': alltime_grade}
    return render(request, 'user/user.html', content)

