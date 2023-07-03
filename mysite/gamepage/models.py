from django.db import models
from django.contrib.auth.models import User
from homepage.models import GameInfo
# Create your models here.


    
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    game = models.ForeignKey(GameInfo,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return str(self.author)+' : '+self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content  = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replies')
    def __str__(self):
        return str(self.author)    
