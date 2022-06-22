from itertools import product
from multiprocessing import context
from re import template
from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from core.models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Web programming with Django framework',
        'outro': 'Django is very good!',
        'inforpro': 'Select one of the products to know the price, and quantity in stock',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contact(request):
    context1 = {
        'contact': 'My contact page'
    }
    return render(request, 'contact.html', context1)


def produto(request, pk):
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)