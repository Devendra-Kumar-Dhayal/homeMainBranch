from django.urls import path
from . import views
from homepage.views import ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('logout/',views.logout_view),
    path('recoverpassword/',ResetPasswordView.as_view()),
    path('new_page.html/<str:pk>',views.rest),

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='homepage/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='homepage/password_reset_complete.html'),
         name='password_reset_complete'),
   
]
