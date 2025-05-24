from django.contrib import admin
from .models import ClothingModel, TypeModel

# Register your models here.
@admin.register(ClothingModel)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'type', 'price')
    list_filter = ('type', 'manufacturer')
    search_fields = ('name', 'manufacturer')

@admin.register(TypeModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = (id,'name')