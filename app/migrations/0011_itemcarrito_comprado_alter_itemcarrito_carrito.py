# Generated by Django 5.0.6 on 2024-07-01 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_itemcarrito_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrito',
            name='comprado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='itemcarrito',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.compra'),
        ),
    ]