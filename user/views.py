from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, Http404
User = get_user_model()


# display user profile
def user(request, username=None):
    if username == None and request.user.is_authenticated:
        return HttpResponseRedirect('/user/' + request.user.username)
    elif username == None:
        raise Http404("You are not logged in")
    user = User.objects.filter(username=username).first()
    if user == None:
        raise Http404("User does not exist")
    content = {'user': user, 'is_self': request.user == user}
    return render(request, 'user/user.html', content)
