# Generated by Django 4.2 on 2024-10-22 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('rol', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Visu5Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso_4', models.BooleanField(default=False)),
                ('porcentaje', models.IntegerField(default=0)),
                ('dias', models.IntegerField(default=0)),
                ('porque', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='porque.porque')),
            ],
        ),
    ]
