from django.shortcuts import render
from django.http import HttpResponseRedirect
from homepage.models import GameInfo
from .forms import PostForm
from .models import Post,Comment
# Create your views here.
def gamePage(request):
     return render(request,'gamepage/index.html')

def getCommentData(comments,post):

    i =0
    data ={}
    comment = {}
    numComments= len(comments)
    if numComments==0:
        return comment
    for comment in comments:
        commentFlag =Comment.objects.filter(post=post).filter(parent=comment).exists()
        if commentFlag : 
            data[comment]=getCommentData(Comment.objects.filter(post=post).filter(parent=comment),post)
        else :
            data[comment]={}
    return data
    
def gamepage(request,id):
    posts={}
    comment = []
    game = GameInfo.objects.get(id=id)
    postsFlag = Post.objects.all().filter(game = game.id ).exists()
    if postsFlag:
        posts = Post.objects.all().filter(game = game.id )
        for post in posts:
        
            commentFlag =Comment.objects.filter(post=post).filter(parent=None).exists()
            if commentFlag : 
                comment=Comment.objects.filter(post=post).filter(parent=None)
    
    data = getCommentData(comment,posts[0])
    print("parent = ",data)
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
        'data':data,
        'comment':comment,
        'posts':posts,
        'game':game,
        'form':form,
    }
    return render(request,'gamepage/index.html',context)