# Generated by Django 4.2 on 2024-11-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniProyecto', '0023_remove_miniproyecto_moc_remove_miniproyecto_moc_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniproyecto',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
    ]