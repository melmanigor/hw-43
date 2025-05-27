from django.shortcuts import render

import requests
def home(request):
    return render(request, 'home.html')
def address(request):
    return render(request, 'address.html')

