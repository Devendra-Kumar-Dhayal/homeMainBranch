from django.shortcuts import render
from django.http import HttpResponseRedirect
from homepage.models import GameInfo
from .forms import PostForm,CommentForm
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
        data[comment] = []
        if commentFlag : 
            data[comment].append(getCommentData(Comment.objects.filter(post=post).filter(parent=comment),post))
        
    return data
    
def gamepage(request,id):
    posts={}
    comment = []
    postData =[]
    game = GameInfo.objects.get(id=id)
    postsFlag = Post.objects.all().filter(game = game.id ).exists()
    if postsFlag:
        posts = Post.objects.all().filter(game = game.id )
        for post in posts:
            
            commentFlag =Comment.objects.filter(post=post).filter(parent=None).exists()
            if commentFlag : 
                comment=Comment.objects.filter(post=post).filter(parent=None)
                postData.append({post:getCommentData(comment,post)})
            else:
                postData.append({post:[]})
    
     
    getCommentData(comment,posts[0])
    
    postForm = PostForm(request.POST or None)
    commentForm = CommentForm(request.POST or None)
    
    if request.method=="POST":
        
        if postForm.is_valid():
            postobj= Post()
            postobj.title = postForm.cleaned_data.get('title')
            postobj.content  = postForm.cleaned_data.get('content')
            postobj.author=request.user
            postobj.game = game
            # print("\n " +postobj.game+"\n")
            postobj.save()
            return HttpResponseRedirect(request.path_info)
        if commentForm.is_valid():
            commentobj = Comment()
            commentobj.title = commentForm.cleaned_data.get('content')
            commentobj.author = request.user
            commentobj.post = Post.objects.get(id = int(commentForm.cleaned_data.get('postid')))
            if CommentForm.objects.get(id = int(commentForm.cleaned_data.get('commentid'))).exists():
                commentobj.parent = CommentForm.objects.get(id = int(commentForm.cleaned_data.get('commentid')))
            else:
                commentobj.parent = ''
    newData = str(postData)
    context = {
        'data':newData,
        'comment':comment,
        'posts':posts,
        'game':game,
        'postForm':postForm,
        'commentForm':commentForm
        
    }
    return render(request,'gamepage/index.html',context)