from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Customer(models.Model):
    SEXE=(('Femme','Femme'),('Homme','Homme'))
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    sexe=models.CharField(choices=SEXE,max_length=5,null=True)
    phone=models.CharField(null=True,max_length=10)
    adresse=models.CharField(null=True,max_length=100)
    city=models.CharField(null=True,max_length=50)
    state=models.CharField(blank=True, max_length=20)
    image=models.ImageField(blank=True,default='person.png')
    bio=RichTextUploadingField()

    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name +' '+ self.user.last_name 
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
