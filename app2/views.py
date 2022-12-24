from django.shortcuts import render
from django.http import *

# Create your views here.
def apple(request):
    return HttpResponse('apple keeps docter away')
