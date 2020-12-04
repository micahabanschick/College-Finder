from django.http.response import HttpResponse
from django.shortcuts import render


def login_page(request):
    return render(request, 'users/login.html', {'mode': 'signin'})


def register_page(request):
    return render(request, 'users/login.html', {'mode': 'signup'})


def submit(request):
    data = request.POST
    print(data)
    return render(request, 'users/login.html', {'mode': 'signup'})
