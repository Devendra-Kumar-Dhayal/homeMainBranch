from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gamePage(request):
     return render(request,'gamepage/index.html')

