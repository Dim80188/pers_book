from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    # if request.method == 'POST':
    #     # new_item_text = request.POST['item_text']
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/one-and-only-list-in-the-world/')



    return render(request, 'home.html')

def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/one-and-only-list-in-the-world/')
