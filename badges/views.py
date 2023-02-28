from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages

# display badges
def badges(request):
    if request.user.is_authenticated:
        collected = request.user.badges_earned.all()
    else:
        collected = []
    badges = Badge.objects.all()
    return render(request, 'badges/badges.html', {'badges': badges, 'collected': collected})