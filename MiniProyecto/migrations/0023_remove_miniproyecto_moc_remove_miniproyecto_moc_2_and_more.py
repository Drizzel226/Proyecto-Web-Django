# Generated by Django 4.2 on 2024-11-07 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0022_miniproyecto_fecha_inicio2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniproyecto',
            name='MOC',
        ),
        migrations.RemoveField(
            model_name='miniproyecto',
            name='MOC_2',
        ),
        migrations.RemoveField(
            model_name='miniproyecto',
            name='MOC_3',
        ),
        migrations.RemoveField(
            model_name='miniproyecto',
            name='MOC_4',
        ),
    ]
