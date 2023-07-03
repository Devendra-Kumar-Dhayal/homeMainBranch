from django.shortcuts import render

# Create your views here.
def accountView(requests):
    return render(requests,'accounts/data.html')