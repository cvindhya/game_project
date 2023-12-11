from django.contrib import admin
from .models import profile, game
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(profile)

class gameresource(ImportExportModelAdmin):
    def has_export_permission(self, request):
        return False


admin.site.register(game, gameresource)