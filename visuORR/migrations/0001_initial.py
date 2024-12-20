# Generated by Django 4.2 on 2024-12-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ORR', '0004_rename_orr_imagendefinir_orr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisuORRModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso_4', models.BooleanField(default=False)),
                ('paso_5', models.BooleanField(default=False)),
                ('porcentaje', models.IntegerField(default=0)),
                ('dias', models.IntegerField(blank=True, null=True)),
                ('Orr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ORR.orr')),
            ],
        ),
    ]
