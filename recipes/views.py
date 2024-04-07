from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jose',
        'age': 25,
        'is_new': True,
        'fruits': ['Banana', 'Apple', 'Pear'],
        'numbers': [1, 2, 3, 4, 5],
        'person': {
            'name': 'Jose',
            'age': 25,

        }

    })


def contact(request):
    return render(request, 'recipes/contact.html')


def about(request):
    return HttpResponse("About page2.")
