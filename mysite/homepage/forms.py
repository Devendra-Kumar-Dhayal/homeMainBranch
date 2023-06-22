# <!-- Login From -->
# <input type="email" placeholder="Enter your email" name="email" required />
# <input type="password" placeholder="Enter your password" name="password" required />
# <label for="check">Remember me</label>

# <!-- Signup From -->

# <input type="email" placeholder="Enter your email" required />
# <input type="password" placeholder="Create password" required />
# <input type="password" placeholder="Confirm password" required />

from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.models import User
user=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField(label='Username',required = True,widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}), label='Password',required = True)
    check = forms.BooleanField(label='Remember me',required=False)

    class Meta:
        model=user
        fields=[
          
            'username',
            'password',
            
        ]

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        check = self.cleaned_data.get('check')
    

        if username and password:
            user=authenticate(username = username,password=password)

            if not user:
                raise forms.ValidationError('User Does Not Exist')
            
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
        
        return super(UserLoginForm, self).clean(*args,**kwargs)



class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}), label='email',required = True)

    newuser=forms.CharField(label='Username',required = True,widget=forms.TextInput(attrs={"placeholder":"Username"}))
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}), label='Password',required = True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}), label='Confirm Password',required = True)

    class Meta:
        model=user
        fields=[
            'email',
            'newuser',
            'password1',
            'password2',
        ]
    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        newuser = self.cleaned_data.get('newuser')
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if User.objects.filter(username=newuser).exists():
            raise forms.ValidationError("Username is not unique")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")
        if password1!=password2:
            raise forms.ValidationError("Passwords Don't Match")

        # username_qs=user.objects.filter(username = username)
        # if username_qs.exists():
        #     raise forms.ValidationError("Username Already In Use")

        return super(UserRegisterForm, self).clean(*args,**kwargs)