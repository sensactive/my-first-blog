# Generated by Django 2.0.2 on 2018-02-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180219_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, height_field=100, upload_to='images/blog/%Y/%m/%d', verbose_name='Ссылка картинки', width_field=100),
        ),
    ]
