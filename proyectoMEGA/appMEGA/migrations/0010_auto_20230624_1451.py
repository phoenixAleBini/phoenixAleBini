# Generated by Django 3.2.19 on 2023-06-24 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0009_alter_propiedadcontratoaumentos_aumentos_indice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propiedades',
            options={'ordering': ['prop_calle', 'prop_numero', 'prop_piso', 'prop_departamento'], 'verbose_name': 'Propiedad', 'verbose_name_plural': 'Propiedades'},
        ),
        migrations.AlterField(
            model_name='cancelaciondeudacontratoalquiler',
            name='fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cancelaciones', to='appMEGA.deudacontratoalquiler', verbose_name='Cancelación de deuda del contrato de alquiler'),
        ),
        migrations.AlterField(
            model_name='contratoalquilerdeducciones',
            name='fk_Contratoalquilerdeducciones_Propiedadcontratoalquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='propiedades_contrato_alquiler', to='appMEGA.propiedadcontratoalquiler', verbose_name='Contrato de Alquiler de la Propiedad'),
        ),
        migrations.AlterField(
            model_name='deudacontratoalquiler',
            name='fk_Deudacontratoalquiler_Propiedadcontratoalquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='deudas', to='appMEGA.propiedadcontratoalquiler', verbose_name='Contrato de alquiler que contrae deuda'),
        ),
        migrations.AlterField(
            model_name='propiedadcontratoaumentos',
            name='fk_Propiedadcontratoaumentos_Propiedadcontratoalquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='aumentos', to='appMEGA.propiedadcontratoalquiler', verbose_name='Contrato de alquiler'),
        ),
    ]