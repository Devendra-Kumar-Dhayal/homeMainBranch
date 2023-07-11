
from  django.urls import path, include
from .views import accountView

urlpatterns = [
    path('account/', accountView),
]