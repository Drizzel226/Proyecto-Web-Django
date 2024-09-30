# Generated by Django 4.2 on 2024-09-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0008_remove_porque_validado1_remove_porque_validado2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='porque',
            old_name='color1',
            new_name='color_validacion1',
        ),
        migrations.RenameField(
            model_name='porque',
            old_name='color2',
            new_name='color_validacion2',
        ),
        migrations.RenameField(
            model_name='porque',
            old_name='color3',
            new_name='color_validacion3',
        ),
        migrations.RenameField(
            model_name='porque',
            old_name='color4',
            new_name='color_validacion4',
        ),
        migrations.RenameField(
            model_name='porque',
            old_name='color5',
            new_name='color_validacion5',
        ),
        migrations.AddField(
            model_name='porque',
            name='validado1',
            field=models.BooleanField(default=False, verbose_name='Validado (1)'),
        ),
        migrations.AddField(
            model_name='porque',
            name='validado2',
            field=models.BooleanField(default=False, verbose_name='Validado (2)'),
        ),
        migrations.AddField(
            model_name='porque',
            name='validado3',
            field=models.BooleanField(default=False, verbose_name='Validado (3)'),
        ),
        migrations.AddField(
            model_name='porque',
            name='validado4',
            field=models.BooleanField(default=False, verbose_name='Validado (4)'),
        ),
        migrations.AddField(
            model_name='porque',
            name='validado5',
            field=models.BooleanField(default=False, verbose_name='Validado (5)'),
        ),
    ]
