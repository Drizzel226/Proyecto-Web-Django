# Generated by Django 4.2 on 2024-09-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paso1',
        ),
        migrations.AddField(
            model_name='porque',
            name='como_ocurre',
            field=models.TextField(default='', verbose_name='¿Cómo ocurre? Describir desde el punto de vista físico el mecanismo de acción visibilizado en el momento.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='cuando_ocurre',
            field=models.TextField(default='', verbose_name='¿Cuando ocurrió? Producción, arranque, saneado, cambio de formato, mantención, etc.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='descripcion_senal',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción de la señal'),
        ),
        migrations.AddField(
            model_name='porque',
            name='donde_ocurre',
            field=models.TextField(default='', verbose_name='¿Dónde ocurre? Producto, equipo, zona de la máquina, etc.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='falla_funcional',
            field=models.TextField(default='', help_text='Describa la falla funcional que se observó', verbose_name='Falla funcional'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='imagen_falla_funcional',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_fallas/'),
        ),
        migrations.AddField(
            model_name='porque',
            name='que_ocurre',
            field=models.TextField(default='', verbose_name='¿Qué ocurre? ¿En qué parte de la máquina o materal se visualiza el problema?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='quien_presente',
            field=models.TextField(default=1, verbose_name='¿Quién estaba presente cuando ocurrió? ¿El problema pasa en todos los turnos?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='porque',
            name='senal_antes',
            field=models.CharField(choices=[('alarma', 'Alarma'), ('fuga', 'Fuga'), ('cavitacion', 'Cavitación'), ('ruido', 'Ruido'), ('otros', 'Otros'), ('nia', 'N/A')], default='', max_length=100, verbose_name='Señal antes de que ocurra el problema'),
            preserve_default=False,
        ),
    ]