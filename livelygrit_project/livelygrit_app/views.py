import random
from django.shortcuts import render

def get_random_motivational_quote():
    file_path = 'livelygrit_app/static/motivational_texts/motivational_quotes.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
        quote = random.choice(lines).strip()

    return quote


def home(request):
    # Get a random motivational quote
    quote = get_random_motivational_quote()
    return render(request, 'livelygrit_app/home.html', {'quote': quote})

def about_us(request):
    # Get a random motivational quote
    quote = get_random_motivational_quote()
    return render(request, 'livelygrit_app/about_us.html', {'quote': quote})

def services(request):
    # Get a random motivational quote
    quote = get_random_motivational_quote()
    return render(request, 'livelygrit_app/services.html', {'quote': quote})

def contact(request):
    # Get a random motivational quote
    if request.method == 'POST':
        # Извличане на данните от формата
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Създаване на нов обект ContactMessage и запазване на данните в базата данни
        ContactMessage.objects.create(full_name=full_name, email=email, message=message)

        # Изпращане на потвърждение (може да се промени съобщението)
        return HttpResponse('Thank you for your message! We will get back to you soon.')

    return render(request, 'livelygrit_app/contact.html')