# Generated by Django 3.0.7 on 2020-06-26 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='availble',
            new_name='available',
        ),
    ]
