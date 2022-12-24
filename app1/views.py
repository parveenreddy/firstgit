from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def praveen(request):
    return HttpResponse('<marquee><h1>PRAVEEN KUMAR REDDY</h1></marquee>')

def arief(request):
    return HttpResponse('<marquee><h1>SYED ARIEF</h1></marquee>')

def arief(request):
    return HttpResponse('<i>iam very very good boy</i>')