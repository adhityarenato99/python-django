from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2")