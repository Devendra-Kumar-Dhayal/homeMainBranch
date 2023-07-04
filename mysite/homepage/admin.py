from django.contrib import admin
from .models import GameInfo
from .models import GameImage
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class GameResource(resources.ModelResource):
	class Meta:
		model = GameInfo	

class GameAdmin(ImportExportModelAdmin):
	resource_class = GameResource

class GameImgResource(resources.ModelResource):
	class Meta:
		model = GameImage	

class GameImgAdmin(ImportExportModelAdmin):
	resource_class = GameImgResource

admin.site.register(GameImage, GameImgAdmin)

admin.site.register(GameInfo, GameAdmin)