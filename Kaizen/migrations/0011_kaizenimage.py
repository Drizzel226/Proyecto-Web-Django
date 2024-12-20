# Generated by Django 4.2 on 2024-11-18 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kaizen', '0010_delete_kaizenimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='KaizenImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
                ('width', models.FloatField(default=100)),
                ('height', models.FloatField(default=100)),
                ('kaizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kaizen_images', to='Kaizen.kaizen')),
            ],
        ),
    ]
