from django.contrib import admin
from appMEGA.models import Paises, Provincias, Poblaciones,  Tipodoc, Tipoprop,Tipocontrato,Tipocesecontrato, Clientes, Empresas, Contratos, Propiedades,  Propiedadcontratoalquiler, Liquidacionencabezado, Comprobantesencabezado, Liquidaciondetalle, Comprobantedetalle, Bancos, Empleados, Tipopagos, Pagos, Propiedadcontratogarante, Propiedadcontratoaumentos, Tipodeduccion, Proveedores, Propiedadeducciones, Secuenciacomprobante, Propiedadcontratoalquiler_INTERMEDIA_Clientes, Contratoalquilerdeducciones, Deudacontratoalquiler, Cancelaciondeudacontratoalquiler
from django import forms

from django.forms import Media

from django.contrib.admin.views.main import ChangeList


from django.urls import path
from django.shortcuts import redirect
from django.shortcuts import render


from django.urls import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404



class PaisesAdmin(admin.ModelAdmin):
    list_display = ("pais_descripcion",)


class ProvinciasAdmin(admin.ModelAdmin):
    list_display = ('provincia_descripcion',)


class PoblacionesAdmin(admin.ModelAdmin):
    list_display = ('poblacion_descripcion','codigo_postal')



class TipodocAdmin(admin.ModelAdmin):
    list_display=("tipo_doc_descripcion", "tipo_doc_estado",)

class TipopropAdmin(admin.ModelAdmin):
    list_display=("tipo_prop_descripcion", "tipo_prop_estado",)

class TipocontratoAdmin(admin.ModelAdmin):
    list_display=("tipo_contrato_descripcion", "tipo_contrato_estado",)

class TipocesecontratoAdmin(admin.ModelAdmin):
    list_display=("tipo_cese_contrato_descripcion", "tipo_cese_contrato_estado",)

class ClientesAdmin(admin.ModelAdmin):
    list_display=("cl_apellido1", "cl_apellido2", "cl_nombre1", "cl_nombre2", "cl_razon_social", "cl_documento", "cl_calle", "cl_numero", "cl_piso", "cl_departamento", "cl_telefono1", "cl_telefono2", "cl_email", "cl_observaciones", "cl_estado",)

class EmpresasAdmin(admin.ModelAdmin):
    list_display=("empresa_apellido1","empresa_apellido2","empresa_nombre1", "empresa_nombre2", "empresa_razon_social", "empresa_tipo", "empresa_calle", "empresa_numero", "empresa_piso", "empresa_departamento","empresa_telefono1", "empresa_telefono2", "empresa_email", "empresa_observaciones", "empresa_documento", "empresa_estado",)

class ContratosAdmin(admin.ModelAdmin):
    list_display=("fecha_inicio_contrato", "fecha_cese_contrato", "contratos_estado", "contratos_observaciones",)

class PropiedadesAdmin(admin.ModelAdmin):
    list_display=("prop_calle", "prop_numero", "prop_piso", "prop_departamento", "protocolo", "fecha_compra", "valor_compra", "fecha_venta", "valor_venta", "sup_construida", "ano_construccion", "habitaciones", "banos", "aseos", "cocina", "terraza", "observaciones",)





class ComprobantesencabezadoAdmin(admin.ModelAdmin):
    list_display=("comprobantes_enc_numero", "comprobantes_enc_fecha",)



class LiquidaciondetalleAdmin(admin.ModelAdmin):
    list_display=("fk_Liquidaciondetalle_Liquidacionencabezado","detalle_liquidacion_monto",)

class ComprobantedetalleAdmin(admin.ModelAdmin):
    list_display=("comprobante_detalle_importe", "comprobante_detalle_iva", "comprobante_detalle_irpf",)

class BancosAdmin(admin.ModelAdmin):
    list_display=("bancos_descripcion", "bancos_estado",)

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=("empleado_legajo", "empleado_documento", "empleado_cuil", "empleado_fecha_alta", "empleado_fecha_baja", "empleado_fecha_nac", "empleado_apellido", "empleado_nombre", "empleado_calle", "empleado_numero", "empleado_piso", "empleado_departamento", "empleado_telefono1", "empleado_telefono2", "empleado_fax", "empleado_email", "empleado_categoria", "empleado_estado", "empleado_observaciones",)

class TipopagosAdmin(admin.ModelAdmin):
    list_display=("tipo_pagos_descripcion","tipo_pagos_estado",)

class PagosAdmin(admin.ModelAdmin):
    list_display=("pago_numero", "pago_fecha","pago_importe")

class PropiedadcontratogaranteAdmin(admin.ModelAdmin):
    list_display=("garante", "garante_observaciones",)


class TipodeduccionAdmin(admin.ModelAdmin):
    list_display=("tipo_deduccion_descripcion", "tipo_deduccion_categoria",)

class ProveedoresAdmin(admin.ModelAdmin):
    list_display=("proveedores_descripcion", "proveedores_estado", "proveedores_calle", "proveedores_numero", "proveedores_piso", "proveedores_departamento", "proveedores_telefono1", "proveedores_telefono2", "proveedores_email", "proveedores_estado",)

class PropiedadeduccionesAdmin(admin.ModelAdmin):
    list_display=("fk_Propiedadeducciones_Propiedades", "fk_Propiedadeducciones_Tipodeduccion", "servicios_pago_propiedad", "servicios_medidor", "servicios_iban", "servicios_observaciones",)

class ContratoalquilerdeduccionesAdmin(admin.ModelAdmin):
    list_display=("fk_Contratoalquilerdeducciones_Propiedadeducciones", "servicios_pago_inquilinos",)




class SecuenciacomprobanteAdmin(admin.ModelAdmin):
    list_display = ("tipo_comprobante", "ultimo_numero", "tipo_comprobante_estado",)

class DeudacontratoalquilerAdmin(admin.ModelAdmin):
    list_display = ("fecha_origen_deuda_alquiler", "monto_deuda_alquiler", "fk_Deudacontratoalquiler_Propiedadcontratoalquiler",)






admin.site.register(Paises, PaisesAdmin) 
admin.site.register(Provincias, ProvinciasAdmin)
admin.site.register(Poblaciones, PoblacionesAdmin)

admin.site.register(Tipodoc, TipodocAdmin)
admin.site.register(Tipoprop, TipopropAdmin)
admin.site.register(Tipocontrato, TipocontratoAdmin)
admin.site.register(Tipocesecontrato, TipocesecontratoAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(Contratos, ContratosAdmin)
admin.site.register(Propiedades, PropiedadesAdmin)


admin.site.register(Comprobantesencabezado, ComprobantesencabezadoAdmin)

admin.site.register(Liquidaciondetalle, LiquidaciondetalleAdmin)
admin.site.register(Comprobantedetalle, ComprobantedetalleAdmin)
admin.site.register(Bancos, BancosAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Tipopagos, TipopagosAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(Propiedadcontratogarante, PropiedadcontratogaranteAdmin)

admin.site.register(Tipodeduccion, TipodeduccionAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Propiedadeducciones, PropiedadeduccionesAdmin)

admin.site.register(Secuenciacomprobante, SecuenciacomprobanteAdmin)
admin.site.register(Contratoalquilerdeducciones, ContratoalquilerdeduccionesAdmin) 
admin.site.register(Deudacontratoalquiler, DeudacontratoalquilerAdmin)





# Registro de la tabla intermedia
class Propiedadcontratoalquiler_INTERMEDIA_ClientesInline(admin.TabularInline):
    model = Propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Clientes.through

@admin.register(Propiedadcontratoalquiler)
class PropiedadcontratoalquilerAdmin(admin.ModelAdmin):
    list_display = ("fk_Propiedadcontratoalquiler_Propiedades", "get_clientes","propiedad_contrato_alquiler_fecha_inicio","propiedad_contrato_alquiler_duracion", "propiedad_contrato_alquiler_fecha_cese")
    filter_horizontal = ('fk_Propiedadcontratoalquiler_Clientes',)  
    inlines = [Propiedadcontratoalquiler_INTERMEDIA_ClientesInline]

    def get_clientes(self, obj):
        clientes = obj.fk_Propiedadcontratoalquiler_Clientes.all()
        nombres_clientes = ', '.join([str(cliente) for cliente in clientes])
        return nombres_clientes

    get_clientes.short_description = "Clientes"






class LiquidacionencabezadoAdmin(admin.ModelAdmin):
    list_display = ('liquidacion_enc_fecha', 'fk_Liquidacionenc_Tipocontrato', 'fk_Liquidacionenc_Propiedadcontratoalquiler')

    class Media:
        js = ["admin/js/desplegables_dependientes.js"]  # Ruta al archivo JavaScript personalizado

   
admin.site.register(Liquidacionencabezado, LiquidacionencabezadoAdmin)





# para agregar mensaje de advertencia  además de la intervención en models.py 
# y la creación de propiedadcontratoaumentos_change_list.html 
# agregando automáticamente el parámetro warning=1 a todos los enlaces de visualización 
# de edición en la lista de instancias de Propiedadcontratoaumentos

@admin.register(Propiedadcontratoaumentos)
class PropiedadcontratoaumentosAdmin(admin.ModelAdmin):
    list_display = ['id_aumentos', 'fk_Propiedadcontratoaumentos_Propiedadcontratoalquiler', 'aumentos_indice', 'aumentos_fianza_actualizada', 'aumentos_mensual_actualizado', 'aumentos_observaciones', 'diferencia_fianza']
    change_form_template = 'admin/propiedadcontratoaumentos_change_form.html'  # Asociar la plantilla al formulario de cambio
    fields = ['fk_Propiedadcontratoaumentos_Propiedadcontratoalquiler', 'aumentos_indice'] # Los campos que quiero se visualicen

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        instance = self.get_object(request, object_id)

        if not object_id:
            # No hay un objeto específico, es decir, situación inicial
            return super().changeform_view(request, object_id, form_url, extra_context)

        instance = get_object_or_404(Propiedadcontratoaumentos, pk=object_id)

        if instance.aumentos_indice:
            warning_message = '¡ADVERTENCIA! Si modificas el INDICE de AUMENTO, automáticamente se estarán actualizando el valor de la FIANZA y de la RENTA MENSUAL. No olvides que REQUIERE PREVIO AVISO AL ARRENDATARIO'
            extra_context['warning_message'] = warning_message
            
        return super().changeform_view(request, object_id, form_url=form_url, extra_context=extra_context)




class CancelaciondeudacontratoalquilerAdmin(admin.ModelAdmin):
    list_display = ("fecha_cancelacion_deuda_alquiler", "monto_cancelacion_deuda_alquiler", "fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler", "deudapendiente")

    def deudapendiente(self, obj):
        return obj.deudapendiente

    deudapendiente.short_description = "Deuda Pendiente"


admin.site.register(Cancelaciondeudacontratoalquiler, CancelaciondeudacontratoalquilerAdmin)





