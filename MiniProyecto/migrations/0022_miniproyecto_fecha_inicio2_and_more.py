# Generated by Django 4.2 on 2024-11-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0021_remove_miniproyecto_accion_correctiva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniproyecto',
            name='Fecha_inicio2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='Fecha_inicio2_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='Fecha_inicio2_3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='Fecha_inicio2_4',
            field=models.DateField(blank=True, null=True),
        ),
    ]
