# Generated by Django 4.2 on 2024-11-21 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0017_imagendespues_imagenantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagendespues',
            name='kaizen',
        ),
        migrations.DeleteModel(
            name='ImagenAntes',
        ),
        migrations.DeleteModel(
            name='ImagenDespues',
        ),
    ]
