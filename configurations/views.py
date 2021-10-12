from django.shortcuts import render, redirect
# Create your views here.
from .models import Configuration
from .forms import ConfigurationForm

def configurations(request):
    configs = Configuration.objects.order_by('date_added')
    context = {'configs': configs}
    return render(request, 'configurations/configs.html', context)

def configuration(request, config_id):
    config = Configuration.objects.get(id=config_id)
    return render(request, 'configurations/config.html', {'config': config})

def new_configuration(request):
    if request.method != 'POST':
        form = ConfigurationForm()
    else:
        form = ConfigurationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('configurations:configurations')

    context = {'form': form}
    return render(request, 'configurations/new_config.html', context)

