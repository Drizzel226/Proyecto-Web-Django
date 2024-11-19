# Generated by Django 4.2 on 2024-11-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0005_kaizen_valor_inicial_kaizen_valor_propuesto_final_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenkaizen',
            name='height',
            field=models.CharField(default='100px', max_length=10),
        ),
        migrations.AddField(
            model_name='imagenkaizen',
            name='width',
            field=models.CharField(default='100px', max_length=10),
        ),
        migrations.AddField(
            model_name='imagenkaizen',
            name='x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='imagenkaizen',
            name='y',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='imagenkaizen',
            name='imagen',
            field=models.ImageField(upload_to='kaizen_images/'),
        ),
    ]