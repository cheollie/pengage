from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages

# display prizes
def prizes(request):
    if request.user.is_authenticated:
        collected = request.user.prizes_redeemed.all()
    else:
        collected = []
    prizes = Prize.objects.all()
    return render(request, 'prizes/prizes.html', {'prizes': prizes, 'collected': collected})

# buy prize
def buy_prize(request, prize_id):
    prize = Prize.objects.get(id=prize_id)
    if request.user.is_authenticated:
        if request.user.coins >= prize.coins_required:
            request.user.coins -= prize.coins_required
            request.user.prizes_redeemed.add(prize)
            request.user.save()
            messages.success(request, 'You have successfully redeemed the prize!')
            return HttpResponseRedirect('../', 'GET')
        else:
            messages.error(request, 'You do not have enough coins to redeem this prize!')
            return HttpResponseRedirect('../', 'GET')
    else:
        return Http404('You are not logged in!')

