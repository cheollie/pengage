from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.user, name='user'),
    path('<str:username>/', views.user, name='user'),
]
