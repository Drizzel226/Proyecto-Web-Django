# Generated by Django 4.2 on 2024-11-21 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0020_kaizen_imagen_deploy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenAntes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_antes/')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenDespues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_despues/')),
            ],
        ),
        migrations.RemoveField(
            model_name='kaizen',
            name='Deployement',
        ),
        migrations.RemoveField(
            model_name='kaizen',
            name='imagen_deploy',
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Deployment',
            field=models.TextField(blank=True, null=True, verbose_name='Deployment de perdidas'),
        ),
        migrations.DeleteModel(
            name='ImagenDeploy',
        ),
        migrations.AddField(
            model_name='imagendespues',
            name='kaizen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_despues', to='Kaizen.kaizen'),
        ),
        migrations.AddField(
            model_name='imagenantes',
            name='kaizen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_antes', to='Kaizen.kaizen'),
        ),
    ]