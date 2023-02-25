from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404
User = get_user_model()


# display user profile
def user(request, username=None):
    if username == None and request.user.is_authenticated:
        username = request.user.username
    elif username == None:
        raise Http404("You are not logged in")
    user = User.objects.filter(username=username)[0]
    print(user)
    content = {'user': user}    
    return render(request, 'user/user.html', content)
