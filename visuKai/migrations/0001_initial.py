# Generated by Django 4.2 on 2024-11-28 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Kaizen', '0039_kaizen_fechacierre_acciones_10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisuKaiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso_4', models.BooleanField(default=False)),
                ('porcentaje', models.IntegerField(default=0)),
                ('dias', models.IntegerField(blank=True, null=True)),
                ('MiniProyecto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Kaizen.kaizen')),
            ],
        ),
    ]
