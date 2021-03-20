from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user_name','sexe','adresse','phone','image_tag']
    
admin.site.register(Customer,CustomerAdmin)