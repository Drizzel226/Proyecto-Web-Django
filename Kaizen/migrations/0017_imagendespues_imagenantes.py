# Generated by Django 4.2 on 2024-11-21 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0016_remove_imagendespues_kaizen_delete_imagenantes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenDespues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_despues/')),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_despues', to='Kaizen.kaizen')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenAntes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_antes/')),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_antes', to='Kaizen.kaizen')),
            ],
        ),
    ]
