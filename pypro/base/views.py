# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def wrigger_error(request):
    1 / 0
