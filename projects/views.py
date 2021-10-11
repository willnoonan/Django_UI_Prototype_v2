from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from configurations.models import Configuration
# Create your views here.


def projects(request):
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def new_project(request):
    configurations = Configuration.objects.all()
    if request.method != 'POST':
        form = ProjectForm()
    else:
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {'form': form, 'configurations': configurations}
    return render(request, 'projects/new_project.html', context)