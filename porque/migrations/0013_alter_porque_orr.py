# Generated by Django 4.2 on 2024-12-18 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORR', '0004_rename_orr_imagendefinir_orr_and_more'),
        ('porque', '0012_porque_orr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porque',
            name='orr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='porques', to='ORR.orr'),
        ),
    ]
