from django.contrib import admin
from django.conf import settings
from .models import ContactInfo,Contact,Setting,FAQ

class ContactAdmin(admin.ModelAdmin):
    list_display=['create_at','subject','email','message']
    list_filter=['subject']
    
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('adresse','phone','email', 'latitude', 'longitude',)
    
    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'update_at']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','create_at','update_at']
    list_filter = ['create_at']


admin.site.register(FAQ,FAQAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Setting,SettingAdmin)