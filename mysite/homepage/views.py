from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate,get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from .forms import UserRegisterForm ,UserLoginForm
from .models import GameInfo
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

def username_exists(username):
    return User.objects.filter(username=username).exists()



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
    flag = False
    sFlag = False
  
    if request.method == "POST" :
       
        # print("form entry")
        # print(form2.post(request))
        
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # data = username
            login(request, user)

            # return redirect('/')
        elif str(form1.errors)!='<ul class="errorlist"><li>username<ul class="errorlist"><li>This field is required.</li></ul></li><li>password<ul class="errorlist"><li>This field is required.</li></ul></li></ul>':
            flag = True
        
        elif form2.is_valid():
            
            user = form2.save(commit=False)
            email= form2.cleaned_data.get('email')
            username = form2.cleaned_data.get('newuser')
            user.username=username
            user.email= email
            password = form2.cleaned_data.get('password1')
           
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
                
            # return redirect('/')
        else :
            sFlag=True
        print(form2.errors)
        print(flag)
        print(sFlag)
            

    context = {
        'form1':form1,
        'form2':form2,
        'game':game,
        'retryLogin':flag,
        'retrySignup':sFlag,
    }
    return render(request, 'homepage/home.html',context)


# def home(request):
#     return render(request,"home.html")


def logout_view(request):
    logout(request)
    return redirect('/')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'homepage/recoverpassword.html'
    email_template_name = 'homepage/password_reset_email.html'
    subject_template_name = 'homepage/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy(home)
