import random
from django.shortcuts import render

def home(request):
    # specify a path to the files with the motivating sentences
    bg_file_path = 'motivational_bg.txt'
    en_file_path = 'motivational_en.txt'

    # open the files and read the sentences
    with open(bg_file_path, encoding='utf-8') as bg_file:
        bg_lines = bg_file.readlines()

    with open(en_file_path, encoding='utf-8') as en_file:
        en_lines = en_file.readlines()

    # choose a random sentence for the current language
    current_language = request.LANGUAGE_CODE
    if current_language == 'bg':
        motivational_line = random.choice(bg_lines).strip()
    else:
        motivational_line = random.choice(en_lines).strip()

    # provide the sentence as the template context
    return render(request, 'livelygrit_app/home.html', {'motivational_line': motivational_line})
