# Generated by Django 5.0.12 on 2025-03-05 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bike_type', models.CharField(choices=[('standard', 'Standard'), ('cargo', 'Cargo')], default='standard', max_length=20)),
                ('status', models.CharField(choices=[('available', 'Available'), ('in_use', 'In Use'), ('maintenance', 'Maintenance'), ('locked', 'Locked')], default='available', max_length=20)),
                ('last_maintenance_at', models.DateTimeField(blank=True, null=True)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bikes', to='stations.station')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
