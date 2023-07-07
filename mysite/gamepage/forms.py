from django import forms
from .models import Comment, Post
class PostForm(forms.Form):
    title=forms.CharField(label='title',required = True,widget=forms.TextInput(attrs={"placeholder":"title"}))
    content = forms.CharField(label='content',required = True,widget=forms.TextInput(attrs={"placeholder":"Your post is about .."}))
    class Meta:
        fields=[
            'title',
            'content', 
        ]
    def post(self,request):
        form = PostForm(request.POST)
        for field in form:
            print("Post Form Field error:",  field.name,field.errors)
    def clean(self,*args,**kwargs):
    
        title= self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')

        if title== ' 'or title==None:
            raise forms.ValidationError('invalid title')
        if content== ' 'or content==None:
            raise forms.ValidationError('invalid content')
        return super(PostForm,self).clean(*args,**kwargs)
    
class CommentForm(forms.Form):
    
    content = forms.CharField(label='content',required = True,widget=forms.TextInput(attrs={"placeholder":"Your comment is ..."}))
    postid = forms.IntegerField(widget=forms.HiddenInput(attrs={'class':'some_class','id':'some_id'}))
    commentid = forms.IntegerField(widget=forms.HiddenInput(attrs={'class':'some_class','id':'some_id'}),required=False)
    class Meta:
        fields=[
            'content', 
            'postid',
            'commentid',
        ]
    def setCid(self,cid):
        self.commentid=forms.IntegerField(widget=forms.HiddenInput(attrs={'class':'some_class','id':'some_id'}),required=False,initial=cid)
    def setPid(self,pid):
        self.postid = forms.IntegerField(widget=forms.HiddenInput(attrs={'class':'some_class','id':'some_id'}),initial=pid)
        
    def post(self,request):
        form = CommentForm(request.POST)
        for field in form:
            print("Post Form Field error:",  field.name,field.errors)
    def clean(self,*args,**kwargs):
    
        content = self.cleaned_data.get('content')
        postid = self.cleaned_data.get('postid')
        
        if Post.objects.filter(id = postid).exists()==False:
            raise forms.ValidationError('invalid post id')
        
        
        
        if content== ' 'or content==None:
            raise forms.ValidationError('invalid content')
        
        return super(CommentForm,self).clean(*args,**kwargs)