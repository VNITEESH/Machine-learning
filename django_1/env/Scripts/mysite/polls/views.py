from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def index(request):
    return HttpResponse("Hello, Django!")

def name(request):
    return HttpResponse("haii my name is niteesh")

def time(request):
    return HttpResponse(date.today())