from django.db import models

# Create your models here.
class GameInfo(models.Model):
	id = models.BigIntegerField(primary_key=True)
	game_name = models.CharField(max_length=100)

	def __str__(self):
		return self.game_name

'''class GameImage(models.Model):
	game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	#images = models.ImageField()'''
