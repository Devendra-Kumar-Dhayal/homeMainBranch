from django.urls import path,include
from . import views
from homepage.views import ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name= 'home'),
    path('logout/',views.logout_view),
    path('recoverpassword/',ResetPasswordView.as_view()),
    

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='homepage/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='homepage/password_reset_complete.html'),
         name='password_reset_complete'),

    path("", include("allauth.urls")),
    
   
]
