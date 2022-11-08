from django.shortcuts import render

from apps.settings.models import Setting
from apps.flower.models import Flower, Sort, Plantation

def products(request):
    settings = Setting.objects.latest('id')
    flowers = Flower.objects.all()
    sorts = Sort.objects.all()
    plantations = Plantation.objects.all()
    return render(request, 'lk-offer.html', locals())