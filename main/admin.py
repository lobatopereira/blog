from django.contrib import admin
from main.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PortfolioResource(resources.ModelResource):
    class Meta:
        model = Portfolio

class PortfolioAdmin(ImportExportModelAdmin):
	resource_classes = [PortfolioResource]

admin.site.register(Portfolio,PortfolioAdmin)

admin.site.register(Categoria)
admin.site.register(Project)
admin.site.register(Post)
