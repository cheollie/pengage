from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.events, name='events'),
    path('<str:event_id>/', views.full_event, name='full_event'),
]
