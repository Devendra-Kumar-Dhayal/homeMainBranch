from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate,get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from .forms import UserRegisterForm ,UserLoginForm






# Create your views here.
def home(request):
    
    form1 = UserLoginForm(request.POST or None )
    form2 = UserRegisterForm(request.POST or None)
    data = "NOt logged in"
    if request.method == "POST" :
       
        print("form entry")
        print(form2.post(request))
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            data = "logged up"
        elif form2.is_valid():
            user = form2.save(commit=False)
            
            password = form2.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            
            data ="signed up"
            

    context = {
        'data': data,
        'form1':form1,
        'form2':form2
    }
    return render(request, 'homepage/home.html',context)



  


# def home(request):
#     return render(request,"home.html")

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')