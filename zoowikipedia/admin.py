from django.contrib import admin

# Register your models here.
from .models import *

class ClassisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'info')

class OrdoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'info')

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'info')

admin.site.register(Classis, ClassisAdmin)
admin.site.register(Ordo, OrdoAdmin)
admin.site.register(Familia,FamiliaAdmin)

