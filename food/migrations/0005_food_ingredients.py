# Generated by Django 3.1.7 on 2021-03-21 13:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_food_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Ingredients',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
    ]
