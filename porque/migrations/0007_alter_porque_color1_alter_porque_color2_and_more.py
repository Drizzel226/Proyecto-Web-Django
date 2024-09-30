# Generated by Django 4.2 on 2024-09-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0006_porque_color1_porque_color2_porque_color3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porque',
            name='color1',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AlterField(
            model_name='porque',
            name='color2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AlterField(
            model_name='porque',
            name='color3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AlterField(
            model_name='porque',
            name='color4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AlterField(
            model_name='porque',
            name='color5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
    ]
