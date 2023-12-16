# Generated by Django 3.2.19 on 2023-06-10 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0004_auto_20230603_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedadeducciones',
            name='fk_Propiedadeducciones_Proveedores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='appMEGA.proveedores', verbose_name='Proveedor'),
        ),
        migrations.AlterField(
            model_name='propiedadeducciones',
            name='servicios_observaciones',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='tipodeduccion',
            name='tipo_deduccion_descripcion',
            field=models.CharField(choices=[('Tasa de basura', 'Tasa de basura (G)'), ('IBI', 'IBI (G)'), ('Comunidad', 'Comunidad (G)'), ('Seguro del hogar', 'Seguro del hogar (G)'), ('Luz', 'Luz (S)'), ('Agua', 'Agua (S)'), ('Gas', 'Gas (S)'), ('Internet', 'Internet (S)'), ('Electricista', 'Electricista (G)'), ('Calefacción', 'Calefacción (G)'), ('Fontanero', 'Fontanero (G)'), ('Manitas', 'Manitas (G)'), ('Aire Acondicionado', 'Aire Acondicionado (G)'), ('Electrodomésticos', 'Electrodomésticos (G)'), ('Calderas', 'Calderas (G)'), ('Persianista', 'Persianista (G)'), ('Albañil', 'Albañil (G)'), ('Gastos venta inmueble', 'Gastos venta inmueble'), ('Otro', 'Otro')], max_length=30, verbose_name='Servicios & Gastos'),
        ),
    ]
