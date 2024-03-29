# Generated by Django 3.2.19 on 2023-09-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0026_auto_20230817_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeduccion',
            name='tipo_deduccion_descripcion',
            field=models.CharField(choices=[('RSU', 'RSU (S)'), ('IBI', 'IBI (G)'), ('Comunidad', 'Comunidad (G)'), ('Seguro del hogar', 'Seguro del hogar (G)'), ('Luz', 'Luz (S)'), ('Agua', 'Agua (S)'), ('Gas', 'Gas (S)'), ('Internet', 'Internet (S)'), ('Electricista', 'Electricista (G)'), ('Calefacción', 'Calefacción (G)'), ('Fontanero', 'Fontanero (G)'), ('Manitas', 'Manitas (G)'), ('Aire Acondicionado', 'Aire Acondicionado (G)'), ('Electrodomésticos', 'Electrodomésticos (G)'), ('Calderas', 'Calderas (G)'), ('Persianista', 'Persianista (G)'), ('Albañil', 'Albañil (G)'), ('Gastos venta inmueble', 'Gastos venta inmueble'), ('Renta', 'Renta (B)'), ('Deuda pendiente', 'Deuda pendiente(B)'), ('Garantía', 'Garantía(B)'), ('Fianza', 'Fianza (B)'), ('Diferencia Fianza', 'Diferencia Fianza (B)'), ('deuda pendiente', 'deuda pendiente'), ('desc.redondeo', 'desc.redondeo'), ('Multa', 'Multa'), ('desc.s/renta (*)', 'desc.s/renta (*)'), ('Otro', 'Otro')], default='0', max_length=30, verbose_name='Concepto deducción'),
        ),
    ]
