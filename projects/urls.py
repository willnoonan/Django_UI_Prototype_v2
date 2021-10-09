"""Defines url patterns for projects app"""

from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('new_project/', views.new_project, name='new_project'),

]