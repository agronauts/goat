from django.shortcuts import render, redirect

from lists.forms import ItemForm
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            item = Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})

def new_list(request):
    list_ = List.objects.create()
    form = ItemForm(data=request.POST)
    if form.is_valid():
        item = Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    list_.delete()
    error = "You can't have an empty list item"
    return render(request, 'home.html', {'form': form})


