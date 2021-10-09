"""Defines url patterns for configurations app"""

from django.urls import path
from . import views

app_name = 'configurations'
urlpatterns = [
    path('configurations/', views.configurations, name='configurations'),
    path('new_configuration/', views.new_configuration, name='new_configuration'),
]