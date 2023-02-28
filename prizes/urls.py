from django.urls import path
from . import views

app_name = 'prizes'
urlpatterns = [
    path('', views.prizes, name='prizes'),
    path('<str:prize_id>/', views.buy_prize, name='buy_prize')
]
