# Generated by Django 4.2 on 2024-11-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0013_remove_miniproyecto_condiciones_basicas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniproyecto',
            name='principio_funcionamiento',
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='condicion_basica',
            field=models.TextField(blank=True, null=True, verbose_name='Condición básica: ¿Existe un estándar (procedimiento/instructivo/formato definido)?, ¿Es conocido por todos, existe un entrenamiento (Registro de capacitación/LUP) ?¿Cumple mantenciones preventivas?'),
        ),
    ]