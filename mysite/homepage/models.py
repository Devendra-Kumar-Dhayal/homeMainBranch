from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class GameInfo(models.Model):

	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=343, default = "demo")
	type = models.CharField(max_length=10, default = "demo")
	required_age = models.IntegerField(default = 0)
	is_free = models.BooleanField(default=False)
	detailed_description = models.CharField(max_length=2000, default = "demo")
	about_the_game = models.CharField(max_length=2000, default = "demo")
	short_description = models.CharField(max_length=2000, default = "demo")
	supported_languages = models.CharField(max_length=100, default = "demo")
	metacritic = models.CharField(max_length=100, default = "demo")
	website = models.URLField(default = "demo")
	header_image = models.ImageField(default='default.jpg')
	capsule_image = models.ImageField(default='default.jpg')
	capsule_imagev5 = models.ImageField(default='default.jpg')
	minimum = models.CharField(max_length=500, default = "demo")
	recommended = models.CharField(max_length=500, default = "demo")
	mac_requirements = models.CharField(max_length=500, default = "demo")
	mac_recommended = models.CharField(max_length=500, default = "demo")
	linux_requirements = models.CharField(max_length=500, default = "demo")
	linux_recommended = models.CharField(max_length=500, default = "demo")
	developers = ArrayField(models.CharField(max_length=100), default= list)
	publishers = ArrayField(models.CharField(max_length=100), default = list)

	def __str__(self):
		return self.name

class GameImage(models.Model):
	id = models.IntegerField(primary_key=True)
	game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	path_thumbnail = models.ImageField(default='default.jpg',max_length=200)
	path_full = models.ImageField(default='default.jpg',max_length=200)


'''
class GameMovies(models.Model):
	id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	movie = models.FileField'''