# Generated by Django 3.2.19 on 2023-06-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0013_cancelaciondeudacontratoalquiler_cancelacion_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsliquidacion',
            name='items_liquidacion_montototal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monto total (incluye iva e IRPF)'),
        ),
        migrations.AlterField(
            model_name='propiedadcontratoalquiler',
            name='propiedad_contrato_alquiler_fianza_origen',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto inicial de fianza'),
        ),
        migrations.AlterField(
            model_name='propiedadcontratoalquiler',
            name='propiedad_contrato_alquiler_mensual_origen',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto mensual al inicio Contrato'),
        ),
        migrations.AlterField(
            model_name='propiedadcontratoalquiler',
            name='propiedad_contrato_alquiler_valor_garantia',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto de la garantía'),
        ),
    ]
