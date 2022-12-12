from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, "homepage/index.html", context)

def about(request):
    context = {}
    return render(request, "homepage/about.html", context)

def contact(request):
    context = {}
    return render(request, "homepage/contact.html", context)

def product1(request):
    context = {}
    return render(request, "homepage/product_1.html", context)

def product2(request):
    context = {}
    return render(request, "homepage/product_2.html", context)

def product3(request):
    context = {}
    return render(request, "homepage/product_3.html", context)

def product4(request):
    context = {}
    return render(request, "homepage/product_4.html", context)
