from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'name': 'Uyen'}
    return render(request, 'rango/about.html',context=context_dict)

def secret(request):
    context_dict = {
        'secret1': 'Hello this is secret number 1.', 
        'secret2': 'Hello this is secret number 2.'
        }
    return render(request, 'rango/secret.html', context=context_dict)