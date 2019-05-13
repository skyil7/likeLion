from django.shortcuts import render
import operator
import re#정규표현식

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = re.split("\W",text)#특수문자 전체 기준으로 split
    wordQuantity = len(words)
    wordDictionary = {}
    textLength = len(text)
    smallLength = len(text)-wordQuantity+1

    while '' in words:
        words.remove('')

    for word in words:
        if word in wordDictionary:
            wordDictionary[word]+=1
        else:
            wordDictionary[word]=1

    wordCount = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)#나온 횟수에 따라 정렬
    return render(request, 'result.html', {'fulltext':text, "words":words, "wq":wordQuantity, "wordCount":wordCount, "textLength":textLength,"smallLength":smallLength}) #text를 담어 같이 전송