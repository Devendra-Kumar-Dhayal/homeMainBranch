from django.shortcuts import render
from django.http import HttpResponse
from .models import GameInfo

game = [
    {'id' :'1', 'name':'game1'},
    {'id' :'2', 'name':'game2'},
    {'id' :'3', 'name':'game3'}
]


def home(request):
    #context = {'game': GameInfo.objects.all}
    context = {'game':game}
    return render(request, 'homepage/home.html', context)


def rest(request, pk):
    return render(request, "new_page.html") 

# Create your views here.
