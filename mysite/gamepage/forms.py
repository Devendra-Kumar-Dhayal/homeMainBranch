from django import forms

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