# Generated by Django 3.2.19 on 2023-06-25 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0015_itemsliquidacion_fk_itemsliquidacion_liquidacionencabezado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsliquidacion',
            name='fk_Itemsliquidacion_Liquidacionencabezado',
        ),
        migrations.RemoveField(
            model_name='itemsliquidacion',
            name='items_liquidacion_montototal',
        ),
    ]
