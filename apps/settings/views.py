from django.shortcuts import render

from apps.settings.models import Setting

def index(request):
    settings = Setting.objects.latest('id')
    context = {
        'settings':settings
    }
    return render(request, 'index.html', context)