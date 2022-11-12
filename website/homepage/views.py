from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This will be the homepage</h1>")
