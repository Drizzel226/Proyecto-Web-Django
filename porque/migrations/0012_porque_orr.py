# Generated by Django 4.2 on 2024-12-17 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORR', '0004_rename_orr_imagendefinir_orr_and_more'),
        ('porque', '0011_imagenfalla'),
    ]

    operations = [
        migrations.AddField(
            model_name='porque',
            name='orr',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='porques', to='ORR.orr'),
            preserve_default=False,
        ),
    ]
