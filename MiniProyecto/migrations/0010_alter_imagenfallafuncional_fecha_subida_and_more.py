# Generated by Django 4.2 on 2024-11-05 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0009_alter_miniproyecto_ahorro_alter_miniproyecto_costo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenfallafuncional',
            name='fecha_subida',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagenfallafuncional',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_fallas/'),
        ),
        migrations.AlterField(
            model_name='imagenfallafuncional',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='MiniProyecto.miniproyecto'),
        ),
    ]
