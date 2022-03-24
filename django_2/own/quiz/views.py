from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  intro(request):
    return HttpResponse('hai hello welcone this is vanama niteesh')
def intro2(request):
    return HttpResponse('hey i am studing in the paruluniversity')
