# Generated by Django 4.2 on 2024-11-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0017_remove_miniproyecto_resumen_miniproyecto_resumen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniproyecto',
            name='Resumen',
        ),
        migrations.AddField(
            model_name='miniproyecto',
            name='resumen',
            field=models.TextField(blank=True, null=True, verbose_name='Resumen del problema'),
        ),
    ]
