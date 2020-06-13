from django.shortcuts import render
from PyDictionary import PyDictionary


dictionary=PyDictionary()


words = []


def index(request):
    return render(request, 'index.html',{
        "words":words
    })


def search(request):
    word = request.GET.get("word")
    word=word.capitalize()
    #Meaning
    meaning = dictionary.meaning(word)
    if word not in words:
        if meaning is not None:
            words.insert(0, word)
    else:
        pass
    return render(request, 'search.html',{
        "word":word,
        "meaning":meaning
    })
