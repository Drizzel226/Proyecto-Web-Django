# Generated by Django 4.2 on 2024-11-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0028_kaizen_seleccion_paso2_alter_kaizen_condicion_basica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_2',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_3',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_4',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_5',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_6',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_7',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='ISHIKAWA_8',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_2',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_3',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_4',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_5',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_6',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_7',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='Raiz_8',
            field=models.TextField(blank=True, null=True, verbose_name='Raíz'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion1_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion2_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion3_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion4_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion5_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion6_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_2',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_3',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_4',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_5',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_6',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_7',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='color_validacion7_8',
            field=models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_2',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_3',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_4',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_5',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_6',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_7',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='modo_falla_paso3_8',
            field=models.TextField(blank=True, null=True, verbose_name='Modo de Falla'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque1_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque2_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque3_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque4_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque5_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque6_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_2',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_3',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_4',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_5',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_6',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_7',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AddField(
            model_name='kaizen',
            name='porque7_8',
            field=models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)'),
        ),
        migrations.AlterField(
            model_name='kaizen',
            name='ISHIKAWA',
            field=models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True),
        ),
    ]
