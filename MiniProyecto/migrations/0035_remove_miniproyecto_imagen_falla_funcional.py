# Generated by Django 4.2 on 2024-11-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0034_miniproyecto_imagen_falla_funcional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniproyecto',
            name='imagen_falla_funcional',
        ),
    ]
