# Generated by Django 4.2 on 2024-11-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0025_remove_miniproyecto_tipo_remove_miniproyecto_tipo_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniproyecto',
            name='estado_2',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='estado_3',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='estado_4',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
    ]
