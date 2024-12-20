# Generated by Django 4.2 on 2024-11-25 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0033_kaizen_estandarizacion_ta_kaizen_expansion_ta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kaizen',
            name='seleccion_paso5',
            field=models.CharField(choices=[('estándar nuevo LUP', 'Estándar nuevo LUP'), ('poka yoke', 'Poka Yoke'), ('gestión visual', 'Gestión Visual'), ('disparador', 'Disparador')], default='no_aplica', max_length=30, null=True, verbose_name='Selección:'),
        ),
        migrations.CreateModel(
            name='ImagenExpansion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_expansion/')),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_expansion', to='Kaizen.kaizen')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_estandar/')),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_estandar', to='Kaizen.kaizen')),
            ],
        ),
    ]
