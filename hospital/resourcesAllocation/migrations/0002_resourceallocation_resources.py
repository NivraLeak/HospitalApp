# Generated by Django 3.0.7 on 2020-06-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_resource_image'),
        ('resourcesAllocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceallocation',
            name='resources',
            field=models.ManyToManyField(through='resourcesAllocation.ResourceAllocationResources', to='resources.Resource'),
        ),
    ]
