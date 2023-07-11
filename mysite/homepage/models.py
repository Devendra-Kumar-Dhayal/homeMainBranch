from django.db import models
from django.contrib.postgres.fields import ArrayField
from import_export.widgets import SimpleArrayWidget

# Create your models here.

'''

changes in `def clean` in `SimpleArrayWidget` class in `import_export`

if type(value) == list:
    if len(value) != 0:
        if type(value[0]) == int:
            value = ",".join(str(num) for num in value)
        else:
            value = ",".join(value)
else:
    pass

'''

class GameInfo(models.Model):

	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=343, default = "demo")
	#type = models.CharField(max_length=10, default = "demo")
	required_age = models.IntegerField(default = 0)
	is_free = models.BooleanField(default=False)
	controller_support = models.CharField(default ="demo")
	dlc = ArrayField(models.IntegerField(),default=list)
	detailed_description = models.CharField(max_length=2000, default = "demo")
	about_the_game = models.CharField(max_length=2000, default = "demo")
	short_description = models.CharField(max_length=2000, default = "demo")
	supported_languages = ArrayField(models.CharField(max_length=100), default=list)
	header_image = models.ImageField(default='default.jpg')
	capsule_image = models.ImageField(default='default.jpg')
	capsule_imagev5 = models.ImageField(default='default.jpg')
	website = models.URLField(default = "demo")
	pc_minimum = models.CharField(max_length=500, default = "demo")
	pc_recommended = models.CharField(max_length=500, default = "demo")
	mac_requirements = models.CharField(max_length=500, default = "demo")
	mac_recommended = models.CharField(max_length=500, default = "demo")
	linux_requirements = models.CharField(max_length=500, default = "demo")
	linux_recommended = models.CharField(max_length=500, default = "demo")
	developers = ArrayField(models.CharField(max_length=100), default= list)
	publishers = ArrayField(models.CharField(max_length=100), default = list)
	windows = models.BooleanField(default=False)
	mac = models.BooleanField(default=False)
	linux = models.BooleanField(default=False)
	metacritic = ArrayField(models.CharField(max_length=200), default=list)
	screenshots =  ArrayField(models.CharField(max_length=200), default=list)
	movies = ArrayField(models.CharField(max_length=200), default=list)
	recommendations = models.IntegerField(default=0)
	coming_soon = models.BooleanField(default=False)
	release_date = models.CharField(default="demo")
	support_url = models.CharField(default="demo")
	support_email = models.CharField(default="demo")
	background = models.ImageField(default="default.jgp")
	background_raw = models.ImageField(default="default.jpg")

	def __str__(self):
		return self.name

class GameCategory(models.Model):	
	game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	id = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=100, default = "demo")

	def __str__(self):
		return self.description

class GameGenre(models.Model):
	game_id = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
	id = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=100, default = "demo")

	def __str__(self):
		return self.description
