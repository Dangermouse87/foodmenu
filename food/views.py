from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader # retrieves a template for a view
from .models import Item # import models for view
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
            'item_list':item_list, # passing the above item list as 'item_list' context
        } # data obtained from db
    return render(request, 'food/index.html', context) # render template, syntax = request, 'html file', context

def detail(request, item_id): # get id to view specific item detail
    item = Item.objects.get(pk=item_id) # Look inside all objects of Item, and get only the item that matches item id (assigned as the item pk)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html', context)

def new(request):
    form = ItemForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/form.html', context)

def update(request, pk): # pass through pk, to get the default primary key, which should be id
    item = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/form.html', {'item':item, 'form':form})

def delete(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/delete.html', {'item':item})
