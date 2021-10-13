"""Defines url patterns for projects app"""

from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('projects/', views.projects, name='projects'),
    # Detail page for a single project.
    path('projects/<int:proj_id>/', views.project, name='project'),
    path('new_project/', views.new_project, name='new_project'),

]