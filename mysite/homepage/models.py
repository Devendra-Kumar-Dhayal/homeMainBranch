from django.db import models

# Create your models here.
class GameInfo(models.Model):
	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=343) #max length is set to 343 because it is 7 cube 
	def __str__(self):
		return self.name

'''class GameImage(models.Model):
	game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	#images = models.ImageField()'''
