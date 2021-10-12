"""Defines url patterns for configurations app"""

from django.urls import path
from . import views

app_name = 'configurations'
urlpatterns = [
    path('configurations/', views.configurations, name='configurations'),
    # Detail page for a single config.
    path('configurations/<int:config_id>/', views.configuration, name='configuration'),
    path('new_configuration/', views.new_configuration, name='new_configuration'),
]