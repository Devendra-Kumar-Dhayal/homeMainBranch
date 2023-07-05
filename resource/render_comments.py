from django.shortcuts import render
from .models import Comment


def render_comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})
