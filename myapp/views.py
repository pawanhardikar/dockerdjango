from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World I am Docker_Django!')

# Create your views here.
