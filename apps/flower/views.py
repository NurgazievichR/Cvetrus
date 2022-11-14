from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.messages import error

from functools import reduce

from apps.settings.models import Setting
from apps.flower.models import Flower, Sort, Plantation
from apps.flower.forms import AddBalanceForm


choices = {
        'plantation':'all',
        'type':'all',
        'sort':'all',
        'length':'all',
        'color':'all',
        'min_price':'0',
        'max_price':'600',
        }

@login_required()
def products(request):
    settings = Setting.objects.latest('id')
    flowers = Flower.objects.all()
    sorts = Sort.objects.all()
    plantations = Plantation.objects.all()
    types =  list(set(reduce(lambda a,b: a+b, Flower.objects.values_list('title'))))  
    length = [str(i) for i in range(30, 101, 20)]
    colors = ['Синий', 'Красный', 'Белый', 'Голубой', 'Жёлтый', 'Чёрный', 'Фиолетовый']

    if 'color_choice' in request.GET:
        choices['color'] = request.GET['color_choice'] if request.GET['color_choice'] != 'color_all' else 'all'
    elif 'length_choice' in request.GET:
        choices['length'] = request.GET['length_choice'] if request.GET['length_choice'] != 'length_all' else 'all'
    elif 'type_choice' in request.GET:
        choices['type'] = request.GET['type_choice'] if request.GET['type_choice'] != 'type_all' else 'all'
    elif 'plantation_choice' in request.GET:
        choices['plantation'] = Plantation.objects.get(id=request.GET['plantation_choice']).title if request.GET['plantation_choice'] != 'plantation_all' else 'all'
    elif 'sort_choice' in request.GET:
        choices['sort'] = Sort.objects.get(id=request.GET['sort_choice']).title if request.GET['sort_choice'] != 'sort_all' else 'all'

    if 'delete_category' in request.GET:
        for k,v in choices.items():
            if v == request.GET['delete_category']:
                choices[k]='all'

    if choices['plantation'] != 'all':
        flowers = flowers.filter(plantation__title = choices['plantation'])
    if choices['sort'] != 'all':
        flowers = flowers.filter(sort__title = choices['sort'])
    if choices['type'] != 'all':
        flowers = flowers.filter(title=choices['type'])
    if choices['length'] != 'all':
        flowers = flowers.filter(length=choices['length'])
    if choices['color'] != 'all':
        flowers = flowers.filter(color=choices['color'])
    if 'price_sort' in request.GET:
        choices['min_price'] = request.GET['from_price']
        choices['max_price'] = request.GET['to_price']

    min_price = choices['min_price']
    max_price = choices['max_price']
    flowers = flowers.filter(price__gte=min_price).filter(price__lte=max_price)

    if 'search_button' in request.GET:
        flowers = Flower.objects.filter(Q(title__istartswith=request.GET['search-field']) | Q(plantation__title__istartswith =request.GET['search-field']) | Q(sort__title__istartswith=request.GET['search-field'])) 

    choices_ = []
    for k,v in choices.items():
        choices_.append(v)

    paginator = Paginator(flowers, 8)
    page_number = request.GET.get('page')
    flowers = paginator.get_page(page_number)

    num_pages = range(1,flowers.paginator.num_pages+1)

    locals()['choices'] = choices
    return render(request, 'lk-offer.html', locals())

@login_required()
def single_product(request, id):
    settings = Setting.objects.latest('id')
    flower = get_object_or_404(Flower, id=id)
    length = [str(i) for i in range(30, 101, 20)]
    flower.views += 1
    flower.save()
    return render(request, 'lk-single.html', locals())

def offers(request):
    settings = Setting.objects.latest('id')
    offers = Flower.objects.all().order_by('-views')[:3]
    return render(request, 'lk.html', locals())


def wallet(request):
    settings = Setting.objects.latest('id')
    form = AddBalanceForm()

    if request.method == 'POST':
        phone = request.POST['phone']
        amount = request.POST['amount']
        user = request.user
        user.balance += int(amount)
        user.save()

    return render(request, 'add-balance.html', locals())


def history_order(request):
    return render(request, 'history-order.html', locals())