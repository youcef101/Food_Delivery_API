from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
class Contact(models.Model):
    subject=models.CharField(max_length=30,null=True)
    adminnote=RichTextUploadingField()
    email=models.EmailField()
    message=models.TextField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class ContactInfo(models.Model):
    adresse=models.CharField(max_length=255,null=True)
    phone=models.CharField(max_length=12,null=True)
    email=models.EmailField()
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.adresse

class Setting(models.Model):
   
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='img/')
    aboutus = RichTextUploadingField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
   
    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
