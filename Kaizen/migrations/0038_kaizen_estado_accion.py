# Generated by Django 4.2 on 2024-11-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0037_kaizen_fechainicio_acciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaizen',
            name='estado_accion',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
    ]
