# Generated by Django 3.0.7 on 2020-06-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20200625_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]