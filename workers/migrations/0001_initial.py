# Generated by Django 4.2.21 on 2025-05-16 14:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('email', models.EmailField(max_length=254)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workers.positionmodel')),
            ],
        ),
    ]
