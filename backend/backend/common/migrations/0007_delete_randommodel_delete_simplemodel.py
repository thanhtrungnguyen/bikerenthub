# Generated by Django 5.0.12 on 2025-03-02 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_remove_simplemodel_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RandomModel',
        ),
        migrations.DeleteModel(
            name='SimpleModel',
        ),
    ]
