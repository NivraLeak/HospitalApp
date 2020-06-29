from django.contrib import admin

from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    fields = ('type','description','available','image')
    list_display = ('__str__','slug')

admin.site.register(Resource,ResourceAdmin)
