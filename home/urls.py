from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('end_quarter/', views.end_quarter, name='end_quarter'),
    path('profile/update/', views.update, name='update'),
]
