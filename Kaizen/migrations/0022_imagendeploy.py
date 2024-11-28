# Generated by Django 4.2 on 2024-11-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0021_imagenantes_imagendespues_remove_kaizen_deployement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenDeploy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_deploy/')),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_deploy', to='Kaizen.kaizen')),
            ],
        ),
    ]