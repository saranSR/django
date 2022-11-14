
import csv
from msilib.schema import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from flask import redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        product_list = Book.objects.filter(name__icontains=q)
    else:
        product_list = Book.objects.all()  
    context = {
        'product_list': product_list
    }
    return render(request,'index.html',context)


def add_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        cost = request.POST['cost']
        book = Book(title=title, author=author, cost=cost)
        book.save()
        messages.info(request,'Added Book')

    else:
        pass

    product_list = Book.objects.all()
    context = {
        'product_list': product_list
    }

    return render(request, 'index.html',context)

def delete_item(request, myid):
    product_list = Book.objects.all()
    context = {
        'product_list': product_list
    }
    product = Book.objects.get(id = myid)
    product.delete()
    messages.info(request,"Record deleted successfully")
    return render(request, 'index.html',context)

def update_item(request,myid):
    sel_item = Book.objects.get(id = myid)
    product_list = Book.objects.all()
    context = {
        'sel_item':sel_item,
        'product_list': product_list
    }
    return render(request, 'index.html',context)

def edit_item(request,myid):
    product = Book.objects.get(id=myid)
    product.title = request.POST['title']
    product.author = request.POST['author']
    product.cost = request.POST['cost']
    product.save()
    product_list = Book.objects.all()
    context = {
        'product_list': product_list
    }
    messages.info(request,"Record deleted successfully")
    return render(request, 'index.html',context)


