from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add

# Create your views here.


def index(request):
    add.delay(1, 4)
    HttpResponse('Hello')
