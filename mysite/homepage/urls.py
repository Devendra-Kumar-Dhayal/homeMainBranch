from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('logout/',views.logout_view),
    path('recoverpassword/',views.recoverpassword),
    path('new_page.html/<str:pk>',views.rest),
]
