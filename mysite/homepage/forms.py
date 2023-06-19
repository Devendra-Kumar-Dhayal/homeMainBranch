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
    newuser=forms.CharField(label='Username',required = True,widget=forms.TextInput(attrs={"placeholder":"Username"}))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}), label='Password',required = True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}), label='Confirm Password',required = True)

    class Meta:
        model=user
        fields=[
          
            'newuser',
            'password1',
            'password2',
        ]
    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
    def clean(self,*args,**kwargs):
        newuser = self.cleaned_data.get('newuser')
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1!=password2:
            raise forms.ValidationError("Passwords Don't Match")

        # username_qs=user.objects.filter(username = username)
        # if username_qs.exists():
        #     raise forms.ValidationError("Username Already In Use")

        return super(UserRegisterForm, self).clean(*args,**kwargs)