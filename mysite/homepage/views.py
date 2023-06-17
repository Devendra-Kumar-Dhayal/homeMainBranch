from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'homepage/home.html')


def rest(request):
    return HttpResponse("rest") 

# Create your views here.
