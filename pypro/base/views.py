from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def trigger_error(request):
    1 / 0
