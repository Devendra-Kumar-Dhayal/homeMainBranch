from django.urls import path,include
from . import views
urlpatterns = [
    path('gamepage/', views.gamePage),
    path("gamepage/<int:id>/",views.gamepage,name='gamepage')
    ]