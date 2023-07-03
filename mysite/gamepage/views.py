from django.shortcuts import render
from django.http import HttpResponseRedirect
from homepage.models import GameInfo
from .forms import PostForm
from .models import Post,Comment
# Create your views here.
def gamePage(request):
     return render(request,'gamepage/index.html')

def gamepage(request,id):
    
    game = GameInfo.objects.get(id=id)
    posts = Post.objects.all().filter(game = game.id )
    # comment = 
    form = PostForm(request.POST or None)
    
    if request.method=="POST":
        
        if form.is_valid():
            postobj= Post()
            postobj.title = form.cleaned_data.get('title')
            postobj.content  = form.cleaned_data.get('content')
            postobj.author=request.user
            postobj.game = game
            # print("\n " +postobj.game+"\n")
            postobj.save()
            return HttpResponseRedirect(request.path_info)
    
    context = {
        'posts':posts,
        'game':game,
        'form':form,
    }
    return render(request,'gamepage/index.html',context)