# Generated by Django 4.2 on 2024-10-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0026_porque_accion_preventiva_porque_accion_correctiva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porque',
            name='Fecha_compromiso1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Fecha_compromiso2',
            field=models.DateField(blank=True, null=True),
        ),
    ]
