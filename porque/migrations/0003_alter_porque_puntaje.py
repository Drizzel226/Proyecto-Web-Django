# Generated by Django 4.2 on 2024-10-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0002_alter_porque_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porque',
            name='puntaje',
            field=models.IntegerField(default=0, null=True),
        ),
    ]