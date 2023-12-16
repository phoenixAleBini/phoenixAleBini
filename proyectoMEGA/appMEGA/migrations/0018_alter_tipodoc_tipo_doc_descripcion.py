# Generated by Django 3.2.19 on 2023-06-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0017_auto_20230627_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodoc',
            name='tipo_doc_descripcion',
            field=models.CharField(blank=True, choices=[('DNI', 'DNI'), ('NIF', 'NIF'), ('CIF', 'CIF'), ('NIE', 'NIE'), ('IVA', 'IVA'), ('PASAPORTE', 'PASAPORTE'), ('Permiso residencia', 'Permiso residencia'), ('LC', 'LC'), ('LE', 'LE'), ('Licencia de Conducir', 'Licencia de Conducir')], max_length=25, null=True, verbose_name='Tipo de Documento'),
        ),
    ]
