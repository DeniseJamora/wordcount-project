from django.http import HttpResponse
from django.shortcuts import render
import operator

def eggs(request):
	return HttpResponse('Eggs are a superfood!')

def home(request):
	return render(request, 'home.html',  {'hey': 'Hello World'})

def count(request):
	fulltext = request.GET['fulltext']
	
	wordlist = fulltext.split()

	dictionary = {}

	for word in wordlist:
		if word in dictionary:
			#Increases the count of that word
			dictionary[word] += 1
		else:
			#Adds new word to dictionary
			dictionary[word] = 1

	sortedwords = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'dictionary':sortedwords})

def about(request):
	return render(request, 'about.html')