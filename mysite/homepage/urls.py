from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('new_page.html/<str:pk>',views.rest)
]
