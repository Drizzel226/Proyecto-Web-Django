# Generated by Django 4.2 on 2024-11-05 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0010_alter_imagenfallafuncional_fecha_subida_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenMiniproyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_miniproyectos/')),
                ('miniproyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='MiniProyecto.miniproyecto')),
            ],
        ),
        migrations.DeleteModel(
            name='ImagenFallaFuncional',
        ),
    ]
