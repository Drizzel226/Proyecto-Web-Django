# Generated by Django 4.2 on 2024-10-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0017_porque_color_validacion1_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porque',
            name='num_filas',
        ),
        migrations.AddField(
            model_name='porque',
            name='Raiz_2',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
    ]