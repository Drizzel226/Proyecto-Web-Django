# Generated by Django 4.2 on 2024-12-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuHAPM', '0002_rename_kaizen_visuhapmmodel_hapm'),
    ]

    operations = [
        migrations.AddField(
            model_name='visuhapmmodel',
            name='paso_5',
            field=models.BooleanField(default=False),
        ),
    ]