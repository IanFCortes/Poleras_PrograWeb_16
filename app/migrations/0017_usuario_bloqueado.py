# Generated by Django 5.0.6 on 2024-07-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_seguimiento_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='bloqueado',
            field=models.BooleanField(default=False),
        ),
    ]
