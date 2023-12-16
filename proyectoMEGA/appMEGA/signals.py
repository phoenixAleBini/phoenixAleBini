from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver
from .models import Propiedadcontratoaumentos, Propiedadcontratoalquiler

# requisito para actualización de variable automática

@receiver(pre_save, sender=Propiedadcontratoaumentos)
def actualizar_mensual_actualizado(sender, instance, **kwargs):
    

    if instance.pk is None:  # Solo se ejecuta en la creación de nuevos objetos
        # Calcula el valor actualizado de aumentos_mensual_actualizado
        instance.aumentos_mensual_actualizado = instance.aumentos_mensual_actualizado * instance.aumentos_indice



@receiver(post_save, sender=Propiedadcontratoalquiler)
def crear_propiedadcontratoaumentos(sender, instance, created, **kwargs):
    if created:
        # Se ha creado un nuevo registro en Propiedadcontratoalquiler
        # Obtener los valores de propiedad_contrato_alquiler_fianza_origen y propiedad_contrato_alquiler_mensual_origen
        fianza_origen = instance.propiedad_contrato_alquiler_fianza_origen
        mensual_origen = instance.propiedad_contrato_alquiler_mensual_origen
        
        # Crear un nuevo registro en Propiedadcontratoaumentos con los valores correspondientes
        Propiedadcontratoaumentos.objects.create(
            fk_Propiedadcontratoaumentos_Propiedadcontratoalquiler=instance,
            aumentos_mensual_actualizado=mensual_origen,
            aumentos_fianza_actualizada=fianza_origen,
            aumentos_indice=1,
            diferencia_fianza=0

        )
