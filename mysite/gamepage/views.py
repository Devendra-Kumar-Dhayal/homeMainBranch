from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Room, Message


@login_required
@csrf_exempt
def comment(request):
    room = Room.objects.all()
    messages = Message.objects.all()

    return render(request, 'gamechat.html', {'room': room, 'message': messages})