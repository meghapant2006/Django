from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello")

def megha(request):
    return HttpResponse("Hello Megha")

def hello(request):
    return HttpResponse("Hello, World!")

def greet(request , name):
    return HttpResponse(f"Hello, {name.capitalize()}!")