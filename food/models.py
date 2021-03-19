from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Food(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=RichTextUploadingField()
    Ingredients=RichTextUploadingField()
    slug=models.SlugField(null=False,unique=True)
    image=models.ImageField(blank=True,null=True,upload_to='img/')
    price=models.DecimalField(max_digits=5,decimal_places=2,default=0)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tilte
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    
    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name='image'
        verbose_name_plural="images"
