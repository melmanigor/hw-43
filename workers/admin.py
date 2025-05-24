from django.contrib import admin
from django.utils.html import format_html
from .models import PositionModel,WorkerModel

# Register your models here.
@admin.register(WorkerModel)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary', 'email', 'position','photo')
    list_filter = ('position',)
    search_fields = ('name', 'email')
    
    def photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover">', obj.photo.url)
        return 'No photo'
    photo.short_description = 'Photo'
@admin.register(PositionModel)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','id')