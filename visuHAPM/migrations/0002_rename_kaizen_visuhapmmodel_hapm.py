# Generated by Django 4.2 on 2024-12-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visuHAPM', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visuhapmmodel',
            old_name='Kaizen',
            new_name='Hapm',
        ),
    ]