# Generated by Django 4.1.3 on 2022-11-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/core/img/products-02.jpg', null=True, upload_to='blog', verbose_name='Imagen'),
        ),
    ]
