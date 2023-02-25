from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


# display events
def leaderboard(request):
    # get users
    users_list = User.objects.order_by('-points')
    content = {'users_list': users_list}    
    return render(request, 'leaderboard/leaderboard.html', content)
