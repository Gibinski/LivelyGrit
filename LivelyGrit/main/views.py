from django.shortcuts import render
import random

def get_random_quote():
    with open('motivational_quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
        return random.choice(quotes).strip()


# Define view functions for each page
def index(request):
    dynamic_text = get_random_quote()
    return render(request, 'base.html', {'dynamic_text': dynamic_text})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
