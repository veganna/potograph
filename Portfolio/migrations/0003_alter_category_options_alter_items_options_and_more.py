# Generated by Django 4.0.1 on 2022-02-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_category_image_alter_items_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ('name',), 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categoties'),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='items'),
        ),
    ]
