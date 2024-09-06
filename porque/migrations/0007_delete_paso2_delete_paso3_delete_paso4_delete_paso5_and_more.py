# Generated by Django 5.0.7 on 2024-09-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porque', '0006_rename_campo1_paso2_campo_1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paso2',
        ),
        migrations.DeleteModel(
            name='Paso3',
        ),
        migrations.DeleteModel(
            name='Paso4',
        ),
        migrations.DeleteModel(
            name='Paso5',
        ),
        migrations.AddField(
            model_name='porque',
            name='campo1_paso3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo1_paso4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo1_paso5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo2_paso3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo2_paso4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo2_paso5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo3_paso3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo3_paso4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo3_paso5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='porque',
            name='campo_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='asunto',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='mensaje',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='porque',
            name='prioridad',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
