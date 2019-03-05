from django.shortcuts import render
from django.http.response import HttpResponse

from .tasks import *

def index(request):
    cele_id = wait.delay()
    return HttpResponse(cele_id)
