# Generated by Django 4.2 on 2024-10-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0006_remove_porque_responsable1_porque_responsable1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porque',
            name='Responsable1',
        ),
        migrations.AddField(
            model_name='porque',
            name='Responsable1',
            field=models.ManyToManyField(blank=True, related_name='responsable1', to='porque.miembroequipo'),
        ),
    ]
