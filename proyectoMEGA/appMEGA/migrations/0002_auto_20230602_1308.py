# Generated by Django 3.2.19 on 2023-06-02 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMEGA', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propiedadeducciones',
            options={'verbose_name': 'Deducciones de la Propiedad'},
        ),
        migrations.RenameField(
            model_name='propiedadeducciones',
            old_name='fk_Propiedadservicios_Propiedades',
            new_name='fk_Propiedadeducciones_Propiedades',
        ),
        migrations.RenameField(
            model_name='propiedadeducciones',
            old_name='fk_Propiedadservicios_Proveedores',
            new_name='fk_Propiedadeducciones_Proveedores',
        ),
        migrations.RenameField(
            model_name='propiedadeducciones',
            old_name='fk_Propiedadservicios_Tipodeduccion',
            new_name='fk_Propiedadeducciones_Tipodeduccion',
        ),
    ]