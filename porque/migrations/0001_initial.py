# Generated by Django 4.2 on 2024-10-22 19:40

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
                ('tarjetas_atrasadas', models.CharField(choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay tarjetas atrasadas o pendientes asociadas a la falla funcional?')),
                ('lila_asociado', models.CharField(choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay LILA asociado a la máquina?')),
                ('ejecuto_lila', models.CharField(choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Se ejecutó correctamente el LILA?')),
                ('mantenimiento_no_ejecutado', models.CharField(choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Hay actividades de mantenimiento no ejecutadas asociadas a la falla funcional (revisar plan de 52 semanas)?')),
                ('materiales_calidad', models.CharField(choices=[('no', 'NO'), ('no_aplica', 'NO APLICA'), ('si', 'SI')], default='no_aplica', max_length=10, null=True, verbose_name='¿Los materiales cumplen con las especificaciones de calidad?')),
                ('modo_falla_paso2', models.TextField(blank=True, null=True, verbose_name='El modo de falla corresponde al evento o situación que causa la falla funcional. Ej: presión inestable por válvula rota, inspector detecta elemento extraño pero no lo rechaza, inspector no detecta elemento extraño, sulfatación de sensor de seguridad, etc.')),
                ('imagen_falla', models.ImageField(blank=True, null=True, upload_to='imagenes_falla/')),
                ('modo_falla_paso3', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_2', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_2', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_3', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_3', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_4', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_4', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_5', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_5', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_6', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_6', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_7', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_7', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('modo_falla_paso3_8', models.TextField(blank=True, null=True, verbose_name='Modo de Falla')),
                ('porque1_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (1)')),
                ('porque2_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (2)')),
                ('porque3_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (3)')),
                ('porque4_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (4)')),
                ('porque5_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (5)')),
                ('porque6_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (6)')),
                ('porque7_8', models.TextField(blank=True, null=True, verbose_name='¿POR QUÉ? (7)')),
                ('color_validacion1', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_2', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_3', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_4', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_5', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_6', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_7', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion1_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion2_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion3_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion4_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion5_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion6_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('color_validacion7_8', models.CharField(choices=[('white', 'Blanco'), ('green', 'Verde'), ('red', 'Rojo')], default='white', max_length=10)),
                ('Raiz', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_2', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_3', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_4', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_5', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_6', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_7', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('Raiz_8', models.TextField(blank=True, null=True, verbose_name='Raíz')),
                ('ISHIKAWA', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_2', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_3', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_4', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_5', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_6', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_7', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('ISHIKAWA_8', models.CharField(blank=True, choices=[('Máquina', 'Máquina'), ('Método', 'Método'), ('Medio Ambiente', 'Medio Ambiente'), ('Material', 'Material'), ('Medición', 'Medición'), ('Mano de Obra', 'Mano de Obra')], max_length=100, null=True)),
                ('Accion_correctiva', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso1', models.DateField(blank=True, null=True)),
                ('Accion_correctiva_2', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso1_2', models.DateField(blank=True, null=True)),
                ('Accion_correctiva_3', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso1_3', models.DateField(blank=True, null=True)),
                ('Accion_correctiva_4', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso1_4', models.DateField(blank=True, null=True)),
                ('Accion_Preventiva', models.TextField(blank=True, null=True)),
                ('Accion_Preventiva_2', models.TextField(blank=True, null=True)),
                ('Accion_Preventiva_3', models.TextField(blank=True, null=True)),
                ('Accion_Preventiva_4', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso2', models.DateField(blank=True, null=True)),
                ('Fecha_compromiso2_2', models.DateField(blank=True, null=True)),
                ('Fecha_compromiso2_3', models.DateField(blank=True, null=True)),
                ('Fecha_compromiso2_4', models.DateField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('p', 'P'), ('gv', 'GV'), ('py', 'PY'), ('m', 'M')], max_length=100, null=True)),
                ('tipo_2', models.CharField(blank=True, choices=[('p', 'P'), ('gv', 'GV'), ('py', 'PY'), ('m', 'M')], max_length=100, null=True)),
                ('tipo_3', models.CharField(blank=True, choices=[('p', 'P'), ('gv', 'GV'), ('py', 'PY'), ('m', 'M')], max_length=100, null=True)),
                ('tipo_4', models.CharField(blank=True, choices=[('p', 'P'), ('gv', 'GV'), ('py', 'PY'), ('m', 'M')], max_length=100, null=True)),
                ('Fecha_cierre_paso4', models.DateField(blank=True, null=True)),
                ('Fecha_cierre_paso4_2', models.DateField(blank=True, null=True)),
                ('Fecha_cierre_paso4_3', models.DateField(blank=True, null=True)),
                ('Fecha_cierre_paso4_4', models.DateField(blank=True, null=True)),
                ('MOC', models.CharField(blank=True, choices=[('aplica', 'Aplica'), ('no aplica', 'No aplica')], max_length=100, null=True)),
                ('MOC_2', models.CharField(blank=True, choices=[('aplica', 'Aplica'), ('no aplica', 'No aplica')], max_length=100, null=True)),
                ('MOC_3', models.CharField(blank=True, choices=[('aplica', 'Aplica'), ('no aplica', 'No aplica')], max_length=100, null=True)),
                ('MOC_4', models.CharField(blank=True, choices=[('aplica', 'Aplica'), ('no aplica', 'No aplica')], max_length=100, null=True)),
                ('Estandarizacion', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso3', models.DateField(blank=True, null=True)),
                ('Estandarizacion_2', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso3_2', models.DateField(blank=True, null=True)),
                ('Estandarizacion_3', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso3_3', models.DateField(blank=True, null=True)),
                ('Estandarizacion_4', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso3_4', models.DateField(blank=True, null=True)),
                ('Expansion', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso4', models.DateField(blank=True, null=True)),
                ('Expansion_2', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso4_2', models.DateField(blank=True, null=True)),
                ('Expansion_3', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso4_3', models.DateField(blank=True, null=True)),
                ('Expansion_4', models.TextField(blank=True, null=True)),
                ('Fecha_compromiso4_4', models.DateField(blank=True, null=True)),
                ('areas_aplicacion', models.CharField(blank=True, max_length=500, null=True)),
                ('puntaje', models.IntegerField(blank=True, null=True)),
                ('Responsable1', models.ManyToManyField(blank=True, related_name='responsable1', to='porque.miembroequipo')),
                ('Responsable1_2', models.ManyToManyField(blank=True, related_name='responsable1_2', to='porque.miembroequipo')),
                ('Responsable1_3', models.ManyToManyField(blank=True, related_name='responsable1_3', to='porque.miembroequipo')),
                ('Responsable1_4', models.ManyToManyField(blank=True, related_name='responsable1_4', to='porque.miembroequipo')),
                ('Responsable2', models.ManyToManyField(blank=True, related_name='responsable2', to='porque.miembroequipo')),
                ('Responsable2_2', models.ManyToManyField(blank=True, related_name='responsable2_2', to='porque.miembroequipo')),
                ('Responsable2_3', models.ManyToManyField(blank=True, related_name='responsable2_3', to='porque.miembroequipo')),
                ('Responsable2_4', models.ManyToManyField(blank=True, related_name='responsable2_4', to='porque.miembroequipo')),
                ('Responsable3', models.ManyToManyField(blank=True, related_name='responsable3', to='porque.miembroequipo')),
                ('Responsable3_2', models.ManyToManyField(blank=True, related_name='responsable3_2', to='porque.miembroequipo')),
                ('Responsable3_3', models.ManyToManyField(blank=True, related_name='responsable3_3', to='porque.miembroequipo')),
                ('Responsable3_4', models.ManyToManyField(blank=True, related_name='responsable3_4', to='porque.miembroequipo')),
                ('Responsable4', models.ManyToManyField(blank=True, related_name='responsable4', to='porque.miembroequipo')),
                ('Responsable4_2', models.ManyToManyField(blank=True, related_name='responsable4_2', to='porque.miembroequipo')),
                ('Responsable4_3', models.ManyToManyField(blank=True, related_name='responsable4_3', to='porque.miembroequipo')),
                ('Responsable4_4', models.ManyToManyField(blank=True, related_name='responsable4_4', to='porque.miembroequipo')),
                ('miembros_equipo', models.ManyToManyField(to='porque.miembroequipo')),
            ],
        ),
    ]
