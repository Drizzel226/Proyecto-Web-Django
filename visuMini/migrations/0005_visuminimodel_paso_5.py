# Generated by Django 4.2 on 2024-12-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuMini', '0004_remove_visuminimodel_ups'),
    ]

    operations = [
        migrations.AddField(
            model_name='visuminimodel',
            name='paso_5',
            field=models.BooleanField(default=False),
        ),
    ]