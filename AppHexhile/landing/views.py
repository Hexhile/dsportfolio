from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
 
def cv(request):
    return render(request, 'landing/cv.html')

def home(request):
    return render(request, 'landing/home.html')
