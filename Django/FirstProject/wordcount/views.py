from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split(' ')
    wordQuantity = len(words)
    wordDictionary = {}

    for word in words:
        if word in wordDictionary:
            wordDictionary[word]+=1
        else:
            wordDictionary[word]=1

    return render(request, 'result.html', {'fulltext':text, "words":words, "wq":wordQuantity, "wordCount":wordDictionary.items()}) #text를 담어 같이 전송