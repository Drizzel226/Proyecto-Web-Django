# Generated by Django 5.1.1 on 2024-09-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiembroEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Porque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('subcategoria', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('subarea', models.CharField(blank=True, max_length=100, null=True)),
                ('maquina', models.CharField(blank=True, max_length=100, null=True)),
                ('pilar', models.CharField(blank=True, max_length=100, null=True)),
                ('impacto', models.TextField(blank=True, null=True)),
                ('kpi_iceo', models.CharField(blank=True, max_length=100, null=True)),
                ('kpi_secundario', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_inicio', models.DateField(auto_now_add=True, null=True)),
                ('fecha_cierre', models.DateField(blank=True, null=True)),
                ('que_ocurre', models.TextField(blank=True, null=True, verbose_name='¿Qué ocurre? ¿En qué parte de la máquina o material se visualiza el problema?')),
                ('como_ocurre', models.TextField(blank=True, null=True, verbose_name='¿Cómo ocurre? Describir desde el punto de vista físico el mecanismo de acción visibilizado en el momento.')),
                ('donde_ocurre', models.TextField(blank=True, null=True, verbose_name='¿Dónde ocurre? Producto, equipo, zona de la máquina, etc.')),
                ('cuando_ocurre', models.TextField(blank=True, null=True, verbose_name='¿Cuándo ocurrió? Producción, arranque, saneado, cambio de formato, mantención, etc.')),
                ('quien_presente', models.TextField(blank=True, null=True, verbose_name='¿Quién estaba presente cuando ocurrió? ¿El problema pasa en todos los turnos?')),
                ('senal_antes', models.CharField(blank=True, choices=[('alarma', 'Alarma'), ('fuga', 'Fuga'), ('cavitacion', 'Cavitación'), ('ruido', 'Ruido'), ('otros', 'Otros'), ('nia', 'N/A')], max_length=100, null=True, verbose_name='Señal antes de que ocurra el problema')),
                ('descripcion_senal', models.TextField(blank=True, null=True, verbose_name='Descripción de la señal')),
                ('falla_funcional', models.TextField(blank=True, null=True, verbose_name='Falla funcional')),
                ('imagen_falla_funcional', models.ImageField(blank=True, null=True, upload_to='imagenes_fallas/')),
                ('principio_funcionamiento', models.TextField(blank=True, null=True, verbose_name='Comprender el principio de funcionamiento de la máquina o proceso, incluyendo estándares y parámetros de trabajo')),
                ('imagen_funcionamiento', models.ImageField(blank=True, null=True, upload_to='imagenes_funcionamiento/')),
                ('condiciones_basicas', models.TextField(blank=True, null=True, verbose_name='Verificar condiciones básicas definidas e identificar desviaciones que impacten en el problema')),
                ('tarjetas_atrasadas', models.CharField(blank=True, choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay tarjetas atrasadas o pendientes asociadas a la falla funcional?')),
                ('lila_asociado', models.CharField(blank=True, choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay LILA asociado a la máquina?')),
                ('ejecuto_lila', models.CharField(blank=True, choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Se ejecutó correctamente el LILA?')),
                ('mantenimiento_no_ejecutado', models.CharField(blank=True, choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay actividades de mantenimiento no ejecutadas asociadas a la falla funcional (revisar plan de 52 semanas)?')),
                ('materiales_calidad', models.CharField(blank=True, choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Los materiales cumplen con las especificaciones de calidad?')),
                ('imagen_falla', models.ImageField(blank=True, null=True, upload_to='imagenes_falla/')),
                ('modo_falla', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('validado1', models.BooleanField(default=False, verbose_name='Validado (1)')),
                ('porque2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('validado2', models.BooleanField(default=False, verbose_name='Validado (2)')),
                ('porque3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('validado3', models.BooleanField(default=False, verbose_name='Validado (3)')),
                ('porque4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('validado4', models.BooleanField(default=False, verbose_name='Validado (4)')),
                ('porque5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('miembros_equipo', models.ManyToManyField(to='porque.miembroequipo')),
            ],
        ),
    ]
