# Generated by Django 4.2 on 2024-10-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porque',
            name='Responsable1',
            field=models.ManyToManyField(blank=True, related_name='responsable1', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable1_2',
            field=models.ManyToManyField(blank=True, related_name='responsable1_2', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable1_3',
            field=models.ManyToManyField(blank=True, related_name='responsable1_3', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable1_4',
            field=models.ManyToManyField(blank=True, related_name='responsable1_4', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable2',
            field=models.ManyToManyField(blank=True, related_name='responsable2', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable2_2',
            field=models.ManyToManyField(blank=True, related_name='responsable2_2', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable2_3',
            field=models.ManyToManyField(blank=True, related_name='responsable2_3', to='porque.miembroequipo'),
        ),
        migrations.AlterField(
            model_name='porque',
            name='Responsable2_4',
            field=models.ManyToManyField(blank=True, related_name='responsable2_4', to='porque.miembroequipo'),
        ),
    ]
