from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate,get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from .forms import UserRegisterForm ,UserLoginForm
from .models import GameInfo
from django.views.decorators.csrf import csrf_protect


def rest(request, pk):
    return render(request, "new_page.html") 


game = [
    {'id' :'1', 'name':'game1'},
    {'id' :'2', 'name':'game2'},
    {'id' :'3', 'name':'game3'}
]
# Create your views here.
@csrf_protect
def home(request):
    
    form1 = UserLoginForm(request.POST or None )
    form2 = UserRegisterForm(request.POST or None)
    data = "NOt logged in"
    if request.method == "POST" :
       
        # print("form entry")
        # print(form2.post(request))
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            data = "logged up"
            # return redirect('/')
        
        elif form2.is_valid():
            user = form2.save(commit=False)
            username = form2.cleaned_data.get('newuser')
            user.username=username
            password = form2.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            
            data ="signed up"
            # return redirect('/')
            

    context = {
        'data': data,
        'form1':form1,
        'form2':form2,
        'game':game
    }
    return render(request, 'homepage/home.html',context)


# def home(request):
#     return render(request,"home.html")


def logout_view(request):
    logout(request)
    return redirect('/')

def recoverpassword(request):
    
    return render(request,'homepage/recoverpassword.html')