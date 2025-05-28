from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def address(request):
    return render(request, 'address.html')

