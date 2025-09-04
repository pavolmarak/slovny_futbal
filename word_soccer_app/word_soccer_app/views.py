from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from word_soccer_app.word_soccer_app.models import Player, Word


def home(request):
    all_words = Word.objects.all()
    all_words.delete()
    return render(request, 'word_soccer_app/index.html')


def find_word(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        word = request.POST.get('word').strip()
        new_word = Word(text=word,player_id=1)
        new_word.save()

        # check if word is in the dictionary
        found = False

        with open("static/word_soccer_app/slovak_nouns.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip().lower() == word.lower() and len(line.strip().lower()) > 1:
                    found = True
                    break
        if found:
            return JsonResponse({"result": "present"})
        else:
            return JsonResponse({"result": "not present"})

    return JsonResponse({"message": "Invalid request"}, status=400)
