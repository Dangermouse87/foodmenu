from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader # retrieves a template for a view
from .models import Item # import models for view

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
            'item_list':item_list, # passing the above item list as 'item_list' context
        } # data obtained from db
    return render(request, 'food/index.html', context) # render template, syntax = request, 'html file', context

def item(request):
    return HttpResponse('This is an item view')

def detail(request, item_id): # get id to view specific item detail
    item = Item.objects.get(pk=item_id) # Look inside all objects of Item, and get only the item that matches item id (assigned as the item pk)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html', context)
