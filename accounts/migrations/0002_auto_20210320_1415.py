# Generated by Django 3.1.7 on 2021-03-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='person.png', upload_to=''),
        ),
    ]
