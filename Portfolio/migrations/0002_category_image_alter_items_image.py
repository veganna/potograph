# Generated by Django 4.0.1 on 2022-02-09 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Core/media/images/categoties'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='Core/media/images/items'),
        ),
    ]