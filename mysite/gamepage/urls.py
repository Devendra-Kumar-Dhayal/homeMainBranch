from django.urls import path,include
from . import views
urlpatterns = [
    path('gamepage/', views.gamePage),
    
    ]