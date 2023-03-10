from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.events, name='events'),
    path('<str:event_id>/', views.full_event, name='full_event'),
    path('<str:event_id>/propagate', views.propagate, name='propagate'),
    path('<str:event_id>/admit', views.admit, name='admit'),
    path('<str:event_id>/admit/<str:username>', views.admit_user, name='admit_user'),
]
