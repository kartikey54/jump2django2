from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'hw/index.html')

def sign(request):
    return render(request, 'hw/sign.html')
