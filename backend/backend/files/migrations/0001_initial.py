# Generated by Django 5.0.12 on 2025-03-02 06:25

import backend.files.utils
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=backend.files.utils.file_generate_upload_path)),
                ('original_file_name', models.TextField()),
                ('file_name', models.CharField(max_length=255, unique=True)),
                ('file_type', models.CharField(max_length=255)),
                ('upload_finished_at', models.DateTimeField(blank=True, null=True)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
