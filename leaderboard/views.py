from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


# display events
def leaderboard(request):
    # get users
    users_alltime = User.objects.order_by('-points_alltime')
    users_quarterly = User.objects.order_by('-points_quarterly')
    content = {'users_alltime': users_alltime, 'users_quarterly': users_quarterly}  
    return render(request, 'leaderboard/leaderboard.html', content)
