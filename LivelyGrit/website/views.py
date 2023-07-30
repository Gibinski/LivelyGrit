# website/views.py
from django.shortcuts import render
import random

def get_random_quote():
    with open('motivational_quotes.txt', 'r') as file:
        quotes = file.readlines()
    return random.choice(quotes)


def home(request):
    return render(request, 'home.html', {'quote': get_random_quote()})

def about_us(request):
    return render(request, 'about_us.html', {'quote': get_random_quote()})

def services(request):
    return render(request, 'services.html', {'quote': get_random_quote()})

def careers(request):
    return render(request, 'careers.html', {'quote': get_random_quote()})

def contact_us(request):
    return render(request, 'contact_us.html', {'quote': get_random_quote()})
