# Generated by Django 5.0.7 on 2024-09-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0003_rename_porque5_porque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paso2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('campo2', models.CharField(max_length=200)),
                ('campo3', models.TextField()),
            ],
        ),
    ]
