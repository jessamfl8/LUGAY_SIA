from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.reminder_list, name='reminder_list'),
    path('reminders/add/', views.add_reminder, name='add_reminder'),
]