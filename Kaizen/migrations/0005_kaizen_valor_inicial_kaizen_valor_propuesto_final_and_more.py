# Generated by Django 4.2 on 2024-11-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0004_remove_kaizen_costo_remove_kaizen_impacto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaizen',
            name='valor_inicial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='valor_propuesto_final',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='valor_real_final',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]