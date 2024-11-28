# Generated by Django 4.2 on 2024-11-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0031_alter_kaizen_seleccion_paso4_imagendefinir'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Accion_Preventiva_9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_10',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_6',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_7',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_8',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_cierre_paso4_9',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_10',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_6',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_7',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_8',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_compromiso2_9',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_10',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_6',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_7',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_8',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Fecha_inicio2_9',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_10',
            field=models.ManyToManyField(blank=True, related_name='responsable2_10', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_5',
            field=models.ManyToManyField(blank=True, related_name='responsable2_5', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_6',
            field=models.ManyToManyField(blank=True, related_name='responsable2_6', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_7',
            field=models.ManyToManyField(blank=True, related_name='responsable2_7', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_8',
            field=models.ManyToManyField(blank=True, related_name='responsable2_8', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Responsable2_9',
            field=models.ManyToManyField(blank=True, related_name='responsable2_9', to='Kaizen.miembroequipo'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_10',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_5',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_6',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_7',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_8',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='estado_9',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Cerrada', 'Cerrada')], default='Pendiente', max_length=10),
        ),
    ]