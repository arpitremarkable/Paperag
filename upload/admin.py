from django.contrib import admin
from upload.models import File, Type

class FileAdmin(admin.ModelAdmin):
    fields=('name', )

admin.site.register(File, FileAdmin)
admin.site.register(Type)