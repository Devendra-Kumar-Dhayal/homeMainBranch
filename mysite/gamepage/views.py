from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import GameInfo
# Create your views here.
def gamePage(request):
     return render(request,'gamepage/index.html')

def gamepage(request,id):
    game = GameInfo.objects.get(id=id)

    context = {
        'game':game
    }
    return render(request,'gamepage/index.html',context)