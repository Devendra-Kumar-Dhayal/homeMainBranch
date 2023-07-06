from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from homepage.models import GameInfo
from .forms import PostForm,CommentForm
from .models import Post,Comment
# Create your views here.
def gamePage(request):
     return render(request,'gamepage/index.html')
def commentToStr(comment):
    return "<h4 class='comments'>"+str(comment)+"</h4><br>"
def postToStr(post):
    return r'<div class="message"><h5>'+str(post.author)+':'+ str(post.title)+'</h5><p style=" margin: 3px;">'+str(post.content)+'</p><h6>post id  = '+str(post.id)+'</h6></div>'

def formForComment(request,comment,post):
    return '<form action="." method="POST">'+'<input type="hidden" name="csrfmiddlewaretoken" value="'+str(get_token(request))+'"><input type="text" name="content" placeholder="Your comment is ..." required="" id="id_content">'+'<input type="hidden" name="postid" class="some_class" id="some_id" value='+str(post.id)+'>'+'<input type="hidden" name="commentid" class="some_class" id="some_id" value='+str(comment.id)+'>'+'<button type="submit">reply</button>'+'</form>'

def getCommentData(request,comments,post):

    i =0
    data =""
    numComments= len(comments)
    if numComments==0:
        return data
    for comment in comments:
        commentFlag =Comment.objects.filter(post=post).filter(parent=comment).exists()
        data += "<br>"
        data+= commentToStr(comment)
        data+=formForComment(request,comment,post)
        if commentFlag : 
            data+=getCommentData(request,Comment.objects.filter(post=post).filter(parent=comment),post)
        
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
                postData.append(postToStr(post)+getCommentData(request,comment,post))
            else:
                postData.append(postToStr(post))
    
     
    
    
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
            commentobj.content = commentForm.cleaned_data.get('content')
            commentobj.author = request.user
            commentobj.post = Post.objects.get(id = int(commentForm.cleaned_data.get('postid')))
            if Comment.objects.all().filter(id = int(commentForm.cleaned_data.get('commentid'))).exists():
                commentobj.parent = Comment.objects.all().filter(id = int(commentForm.cleaned_data.get('commentid')))[0]
            else:
                commentobj.parent = None
            commentobj.save()


    newData = postData
    context = {
        'data':newData,
        'comment':comment,
        'posts':posts,
        'game':game,
        'postForm':postForm,
        'commentForm':commentForm
        
    }
    return render(request,'gamepage/index.html',context)