# Generated by Django 5.0.6 on 2024-06-20 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='region',
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]