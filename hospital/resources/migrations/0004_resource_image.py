# Generated by Django 3.0.7 on 2020-06-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_resource_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(default='', upload_to='resources/'),
            preserve_default=False,
        ),
    ]