from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'word_soccer_app/index.html')
