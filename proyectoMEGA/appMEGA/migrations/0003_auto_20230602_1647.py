# Generated by Django 3.2.19 on 2023-06-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0002_auto_20230602_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propiedadcontratoaumentos',
            options={'ordering': ['aumentos_indice'], 'verbose_name': 'Actualización contrato alquiler', 'verbose_name_plural': 'Actualizaciones del contrato de alquiler'},
        ),
        migrations.RemoveField(
            model_name='propiedadcontratoalquiler',
            name='propiedad_contrato_alquiler_fecha_fin',
        ),
        migrations.RemoveField(
            model_name='propiedadcontratoaumentos',
            name='aumentos_fecha_actualizacion',
        ),
        migrations.AlterField(
            model_name='propiedadcontratoaumentos',
            name='aumentos_observaciones',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='propiedadeducciones',
            name='servicios_iban',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Código IBAN-pago serv-'),
        ),
        migrations.AlterField(
            model_name='propiedadeducciones',
            name='servicios_medidor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Medidor servicio'),
        ),
    ]
