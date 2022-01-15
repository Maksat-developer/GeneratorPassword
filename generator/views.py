from django.shortcuts import render
from django.http import HttpResponse
import random

def Home(request):
    return render (request, 'generator/home.html')

def About(request):
    return render (request, 'generator/about.html')

def password(request):
    Characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        Characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()_+}|:"?>><?,./;\|/.'))

    if request.GET.get('number'):
        Characters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 12))

    Thepassword = ''

    for x in range(lenght):
        Thepassword += random.choice(Characters)

    return render (request, 'generator/password.html', {'password': Thepassword})
