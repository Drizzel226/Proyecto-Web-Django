# Generated by Django 4.2 on 2024-11-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0018_remove_imagendespues_kaizen_delete_imagenantes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kaizen',
            old_name='deploy',
            new_name='Deployement',
        ),
    ]