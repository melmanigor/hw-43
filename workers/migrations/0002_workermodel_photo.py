# Generated by Django 4.2.21 on 2025-05-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workermodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='workers_photos/'),
        ),
    ]
