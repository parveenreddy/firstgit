from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sonu(request):
    return HttpResponse('<marquee><i><h1>SAI KRISHNA</h1></i></marquee>')

def sathwik(request):
    return HttpResponse('<marquee><i><h1>SATHWIK MELBOW</h1></i></marquee>')

def smarty(request):
    return HttpResponse('<marquee><i><h1>SMARTY NIKHIL</h1></i></marquee>')