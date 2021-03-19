from django.contrib import admin
import admin_thumbnails
from .models import Food,Images

# Register your models here.
@admin_thumbnails.thumbnail('image')
class FoodImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 4

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class FoodAdmin(admin.ModelAdmin):
    list_display=['title','price','create_at','image_tag']
    list_filter=['title']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    inlines = [FoodImageInline]

admin.site.register(Food,FoodAdmin)
admin.site.register(Images,ImagesAdmin)