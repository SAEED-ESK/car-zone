from django.contrib import admin
from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Car Image'
    
    list_display = ('id', 'thumbnail','car_title', 'city', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail','car_title')
    
    search_fields = ('id', 'car_title', 'model')
    list_filter = ('city', 'model', 'fuel_type')
    list_editable = ('is_featured',)
    
    
admin.site.register(Car, CarAdmin)