from django.contrib import admin
from .models import GameInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class GameResource(resources.ModelResource):
	class Meta:
		model = GameInfo	

class GameAdmin(ImportExportModelAdmin):
	resource_class = GameResource

admin.site.register(GameInfo, GameAdmin)