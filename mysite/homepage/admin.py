from django.contrib import admin
from .models import GameInfo
from .models import GameCategory, GameGenre
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

################################################

class GameResource(resources.ModelResource):
	class Meta:
		model = GameInfo	
		#import_id_fields = ['my_id']

class GameAdmin(ImportExportModelAdmin):
	resource_class = GameResource

################################################

class GameCategoryResource(resources.ModelResource):
	class Meta:
		model = GameCategory	
		import_id_fields = ['id']

class GameCategoryAdmin(ImportExportModelAdmin):
	resource_class = GameCategoryResource

################################################

class GameGenreResource(resources.ModelResource):
	class Meta:
		model = GameGenre	
		import_id_fields = ['id']

class GameGenreAdmin(ImportExportModelAdmin):
	resource_class = GameGenreResource

################################################

admin.site.register(GameGenre, GameGenreAdmin)

admin.site.register(GameCategory, GameCategoryAdmin)

admin.site.register(GameInfo, GameAdmin)