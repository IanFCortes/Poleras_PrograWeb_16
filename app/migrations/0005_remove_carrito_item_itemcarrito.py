# Generated by Django 5.0.6 on 2024-06-28 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_equipo_logo_alter_polera_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='item',
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('subtotal', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('polera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.polera')),
            ],
        ),
    ]
