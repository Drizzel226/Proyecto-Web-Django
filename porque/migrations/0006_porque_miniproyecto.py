# Generated by Django 4.2 on 2024-11-07 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0020_miniproyecto_desarrollo_alter_miniproyecto_ishikawa'),
        ('porque', '0005_alter_porque_fecha_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='porque',
            name='miniproyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='porques', to='MiniProyecto.miniproyecto'),
        ),
    ]
