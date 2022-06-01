from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class DrugsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_show','subcategory')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src= '{}' width='60'/>".format(obj.img.url))
        return ' None'
    image_show.__name__="Картинка"


admin.site.register(Drugs, DrugsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Message)
# admin.site.register(Basket)