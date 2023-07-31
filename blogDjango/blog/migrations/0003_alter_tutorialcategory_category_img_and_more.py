# Generated by Django 4.2.3 on 2023-07-31 09:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_tutorialseries_series_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_img',
            field=models.ImageField(blank=True, upload_to='./media/category_img', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_img',
            field=models.ImageField(blank=True, upload_to='./media/series_img'),
        ),
    ]
