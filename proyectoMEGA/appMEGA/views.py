from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import request

from django.views.decorators.http import require_POST

from .models import Propiedadcontratoalquiler
from django.utils import timezone
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta	

from django.shortcuts import render, get_object_or_404
from appMEGA.models import Propiedadcontratoaumentos, Contratoalquilerdeducciones, Tipodeduccion, Propiedadeducciones, Liquidacionencabezado, Tipocontrato, Liquidaciondetalle, Deudacontratoalquiler, Cancelaciondeudacontratoalquiler, Contratos, Propiedadcontratoalquiler

from django.views import View
from django.http import JsonResponse

from django.db.models import Sum
import json
from django.views.decorators.csrf import csrf_protect

from django.template.loader import render_to_string

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak
from django.http import FileResponse


from django.db.models import OuterRef, Subquery
from django.template import Template, Context
from appMEGA.templatetags import custom_tags
from django.db.models.functions import Lower

import calendar

from django.views.decorators.csrf import csrf_exempt






 



 
			

# Create your views here.

def index(request):
    return render(request, "appMEGA/index.html")

def login(request):   #atiende las peticiones del GET 
    msg=""
    return render(request, "appMEGA/login.html",    
        {"msg":msg,}
    )   # considera mensaje enviado al usuario si los datos no son correctos
        

def indexadmin(request):				
    return render(request, "appMEGA/indexadmin.html")	




def facturas(request):				
    return render(request, "appMEGA/facturas.html")	

def card_liquidacion(request):	

    prop = Propiedadcontratoalquiler.objects.all()
    context = {'object': prop}	

    return render(request, "appMEGA/card_liquidacion.html", context)
		

def liquidMF(request):
    prop = Propiedadcontratoalquiler.objects.all()
    fecha_actual = timezone.now().date()  # Obtener la fecha actual en la zona horaria configurada
    fecha_siguiente = fecha_actual + relativedelta(months=1)  # Obtener el mes siguiente
    mes_actual = fecha_actual.month  # Obtener el número del mes actual
    if mes_actual == 12:  # Si el mes actual es enero
        mes_siguiente = 1 # El mes anterior es diciembre del año anterior
    else:
        mes_siguiente= mes_actual + 1  # Restar 1 al número del mes para obtener el mes anterior
        contador = 1 
    


    ########## 

    lista_tipos_deduccion = []  # Lista para almacenar los tipos de deducción filtrados
    objetos_propiedad = []


    ########## 2
    for objeto in prop:
        propiedades_id = objeto.id_propiedad_contrato_alquiler

        fecha_inicio = objeto.propiedad_contrato_alquiler_fecha_inicio
       



    ########## 3    
        deducciones_filtradas = Contratoalquilerdeducciones.objects.filter(
            fk_Contratoalquilerdeducciones_Propiedadcontratoalquiler=propiedades_id,
            servicios_pago_inquilinos='SI'
        )

        tipos_deduccion_ids = deducciones_filtradas.values_list(
            'fk_Contratoalquilerdeducciones_Propiedadeducciones__fk_Propiedadeducciones_Tipodeduccion',
            flat=True
        )

          # Ordenar las descripciones alfabéticamente en la consulta
        tipos_deduccion_descripciones = Tipodeduccion.objects.filter(
            id_tipo_deduccion__in=tipos_deduccion_ids
        ).order_by(Lower('tipo_deduccion_descripcion')).values_list('tipo_deduccion_descripcion', flat=True)


    ########## 4

        # Crear un diccionario con el ID de la propiedad y la descripción de la deducción
        tipos_deduccion_dict = {
            'propiedad_id': propiedades_id,
            'descripciones': tipos_deduccion_descripciones,
            
        }   

        # Agregar el diccionario a la lista
        lista_tipos_deduccion.append(tipos_deduccion_dict)





       #**********************************************************************************************************************#

       # Obtener la fecha más reciente de Cancelaciondeudacontratoalquiler para el objeto actual de Propiedadcontratoalquiler
        cancelacion_mas_reciente = Cancelaciondeudacontratoalquiler.objects.filter(
            fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler__fk_Deudacontratoalquiler_Propiedadcontratoalquiler=objeto,
            fecha_cancelacion_deuda_alquiler__lte=fecha_actual
        ).order_by('-fecha_cancelacion_deuda_alquiler').first()



        # Obtener el valor de "Deuda Pendiente" más reciente asociado a la fecha más reciente de cancelación de deuda
        deuda_pendiente_mas_reciente = 0
        if cancelacion_mas_reciente:
            deuda_pendiente_mas_reciente = cancelacion_mas_reciente.fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler.monto_deuda_alquiler - cancelacion_mas_reciente.monto_cancelacion_deuda_alquiler



        objetos_propiedad.append({
            'propiedad_id': propiedades_id,
             
            'fecha_mas_reciente': cancelacion_mas_reciente.fecha_cancelacion_deuda_alquiler if cancelacion_mas_reciente else None,
            'deuda_pendiente_mas_reciente': deuda_pendiente_mas_reciente,    
               
        })



        #**********************************************************************************************************************#
        

    context = {
        'object': prop, 
        'fecha_actual': fecha_actual,
        'fecha_siguiente': fecha_siguiente, 
        'lista_tipos_deduccion': lista_tipos_deduccion,
        'form_counter': contador,
        'mes_actual': mes_actual,
        'mes_siguiente':mes_siguiente,
        'objetos_propiedad': objetos_propiedad,  
        

    }
    return render(request, "appMEGA/liquidMF.html", context)














# para mostrar la instancia de Propiedadcontratoaumentos con el parámetro de advertencia:

def propiedadcontratoaumentos_detail(request, pk):
    instance = get_object_or_404(Propiedadcontratoaumentos, pk=pk)
    warning = request.GET.get('warning')
    context = {
        'instance': instance,
        'warning': warning,
    }
    return render(request, 'appMEGA/propiedadcontratoaumentos_detail.html', context)



def obtener_diferencia_fianza(request, id_propiedad_contrato_alquiler):
    instancia = Propiedadcontratoalquiler.objects.get(id=id_propiedad_contrato_alquiler)
    diferencia_fianza = instancia.diferencia_fianza
    data = {'diferencia_fianza': diferencia_fianza}
    return JsonResponse(data)



#  FUNCION NECESARIA PARA PROCESAR FECHA DE LA SIGUIENTE FUNCIÓN QUE TRAE DEL liquidMF  

def get_first_day_of_month(date_str):
    months = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    parts = date_str.split()
    month = months.get(parts[0].lower())
    year = int(parts[1])
    
    return datetime(year, month, 1)


@csrf_protect
def save_Mega_liq_alq(request):
    
    if request.method == 'GET':


        
        # que tenga acceso al modelo Tipodeduccion y al campo tipo_deduccion_descripcion para utilizar en main.js

        tipo_deducciones = Tipodeduccion.objects.all()

        opciones = [tipo_deduccion.tipo_deduccion_descripcion for tipo_deduccion in tipo_deducciones]

        # Devuelve la respuesta JSON con las opciones
        return JsonResponse({'tipo_deduccion_descripcion': opciones})



    elif request.method == 'POST':




        # -----------------parte I: LIQUIDACIÓN ENCABEZADO------------------------------

        fecha_texto = request.POST.get('fecha_actual')

        fecha_convertida = get_first_day_of_month(fecha_texto)


        tipocontrato_id = int(request.POST.get('tipocontrato_id')) # lo convierte en entero
        tipocontrato = Tipocontrato.objects.get(pk=tipocontrato_id)  # Obtén la instancia correcta
        contrato_id= int(request.POST.get('contrato_id'))
        contrato=Contratos.objects.get(pk=contrato_id)
        propiedadcontratoalquiler_id = int(request.POST.get('propiedadcontratoalquiler_id'))

        # Obtener la instancia de Propiedadcontratoalquiler
        propiedadcontratoalquiler=Propiedadcontratoalquiler.objects.get(pk=propiedadcontratoalquiler_id)


        # Crea una instancia de Liquidacionencabezado y guárdala en la base de datos
        liquidacion_encabezado = Liquidacionencabezado(liquidacion_enc_fecha =fecha_convertida,
                                                       fk_Liquidacionenc_Tipocontrato= tipocontrato,
                                                       fk_Liquidacionenc_Contratos= contrato, 
                                                       fk_Liquidacionenc_Propiedadcontratoalquiler=propiedadcontratoalquiler)

        liquidacion_encabezado.save()


        # ------------------------parte II: LIQUIDACIÓN DETALLE -----------------------------

        # Obtener el id_liquidacion_enc recién generado
        id_liquidacion_enc = liquidacion_encabezado.id_liquidacion_enc
        fecha_actual = timezone.now().date()  # Obtener la fecha actual en la zona horaria configurada

        # RENTA ---------------------------------------

        # Obtener el último aumento_mensual_actualizado para esa instancia
        ultimo_aumento_mensual = propiedadcontratoalquiler.propiedadcontratoaumentos_set.last()

        # Verificar si se obtuvo algún aumento
        if ultimo_aumento_mensual:
            ultimo_valor = ultimo_aumento_mensual.aumentos_mensual_actualizado
        else:
            ultimo_valor = 0.00  # Valor por defecto si no hay aumentos

        # Modifica esta parte para incluir la lógica de validación
        iva_value = 0.00
        irpf_value = 0.00

        tipos_prop_validos = ['despacho', 'local comercial', 'nave comercial', 'nave agrícola', 'nave industrial', 'nave logística']

        if propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Tipoprop.tipo_prop_descripcion in tipos_prop_validos:
            iva_value = custom_tags.calcular_valor(propiedadcontratoalquiler)
            irpf_value = custom_tags.calcular_valor2(propiedadcontratoalquiler)

        # Calcular la suma de los valores
        suma_valor = float(ultimo_valor) + float(iva_value) + float(irpf_value)



        tipodeduccion_renta = Tipodeduccion.objects.get(tipo_deduccion_descripcion='Renta')
        liquidacion_detalle = Liquidaciondetalle(
            fk_Liquidaciondetalle_Liquidacionencabezado_id=id_liquidacion_enc,
            fk_Liquidaciondetalle_Tipodeduccion=tipodeduccion_renta,
            detalle_liquidacion_monto=ultimo_valor,
            detalle_liquidacion_iva=iva_value,
            detalle_liquidacion_irpf=irpf_value,
            detalle_liquidacion_debe=suma_valor )

        liquidacion_detalle.save()



        #  FIANZA --------------------------------------

        fianza_actualizada_value = 0.00  # Valor predeterminado

        # Verificar si la fecha de inicio del contrato coincide con la fecha actual
        if propiedadcontratoalquiler.propiedad_contrato_alquiler_fecha_inicio.strftime("%Y-%m") == fecha_actual.strftime("%Y-%m"):
            # Obtener el valor de Fianza Actualizada utilizando el custom tag en el contexto
            context = {'propiedadcontratoalquiler': propiedadcontratoalquiler}
            fianza_actualizada_value = custom_tags.calcular_valor_fianza(propiedadcontratoalquiler)

        # Modifica esta parte para incluir la lógica de validación
        iva_fianza2 = 0.00
        irpf_fianza2 = 0.00

        tipos_prop_validos = ['despacho', 'local comercial', 'nave comercial', 'nave agrícola', 'nave industrial', 'nave logística']

        if propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Tipoprop.tipo_prop_descripcion in tipos_prop_validos:
            iva_fianza2 = custom_tags.calcular_valor_fianza(propiedadcontratoalquiler)
            irpf_fianza2 = custom_tags.calcular_valor_fianza2(propiedadcontratoalquiler)

        suma_valor_fianza = float(fianza_actualizada_value) + float(iva_fianza2) + float(irpf_fianza2)

        # Crear instancia de Liquidaciondetalle para Fianza Original si cumple condiciones
        if fianza_actualizada_value > 0:
            tipodeduccion_fianza_original = Tipodeduccion.objects.get(tipo_deduccion_descripcion='Fianza')
            liquidacion_detalle = Liquidaciondetalle(
                fk_Liquidaciondetalle_Liquidacionencabezado_id=id_liquidacion_enc,
                fk_Liquidaciondetalle_Tipodeduccion=tipodeduccion_fianza_original,
                detalle_liquidacion_monto=fianza_actualizada_value,
                detalle_liquidacion_iva=iva_fianza2,
                detalle_liquidacion_irpf=irpf_fianza2,
                detalle_liquidacion_debe=suma_valor_fianza
            )
            liquidacion_detalle.save()


        # DIFERENCIA FIANZA -------------------------------
        mes_actual = fecha_actual.month  # Obtener el número del mes actual
        mes_siguiente = (mes_actual % 12) + 1  # Obtener el número del mes siguiente

        # Obtener los aumentos que cumplen las condiciones
        aumentos = propiedadcontratoalquiler.propiedadcontratoaumentos_set.filter(
            diferencia_fianza__gt=0,
            aumento_mes_mismo=mes_siguiente,
        )

        diferencia_fianza = 0.0
        iva_diffianza = 0.0
        irpf_diffianza = 0.0

        tipos_prop_validos = ['despacho', 'local comercial', 'nave comercial', 'nave agrícola', 'nave industrial', 'nave logística']

        if propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Tipoprop.tipo_prop_descripcion in tipos_prop_validos:
            # Aplicar condiciones
            for aumento in aumentos:
                diferencia_fianza += aumento.diferencia_fianza
                iva_diffianza += custom_tags.calcular_valor_diffianza(aumento)
                irpf_diffianza += custom_tags.calcular_valor_diffianza2(aumento)

        # Comprobar y asignar un valor predeterminado de 0.0 si el valor es 0 o None
        diferencia_fianza = diferencia_fianza if diferencia_fianza > 0 else 0.0
        iva_diffianza = iva_diffianza if iva_diffianza > 0 else 0.0
        irpf_diffianza = irpf_diffianza if irpf_diffianza > 0 else 0.0

        suma_valor_diffianza = diferencia_fianza + iva_diffianza + irpf_diffianza

        # Crear instancia de Liquidaciondetalle para Diferencia Fianza si cumple condiciones
        if diferencia_fianza > 0:
            tipodeduccion_diffianza = Tipodeduccion.objects.get(tipo_deduccion_descripcion='Diferencia Fianza')
            liquidacion_detalle_diffianza = Liquidaciondetalle(
                fk_Liquidaciondetalle_Liquidacionencabezado_id=id_liquidacion_enc,
                fk_Liquidaciondetalle_Tipodeduccion=tipodeduccion_diffianza,
                detalle_liquidacion_monto=diferencia_fianza,
                detalle_liquidacion_iva=iva_diffianza,
                detalle_liquidacion_irpf=irpf_diffianza,
                detalle_liquidacion_debe=suma_valor_diffianza
            )
            liquidacion_detalle_diffianza.save()


# DEUDA PENDIENTE -----------------------------------      

        # Calcular deuda_pendiente_mas_reciente para la propiedad seleccionada
        cancelacion_mas_reciente = Cancelaciondeudacontratoalquiler.objects.filter(
            fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler__fk_Deudacontratoalquiler_Propiedadcontratoalquiler=propiedadcontratoalquiler,
            fecha_cancelacion_deuda_alquiler__lte=fecha_actual
        ).order_by('-fecha_cancelacion_deuda_alquiler').first()

        deuda_pendiente_mas_reciente = 0
        if cancelacion_mas_reciente:
            deuda_pendiente_mas_reciente = cancelacion_mas_reciente.fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler.monto_deuda_alquiler - cancelacion_mas_reciente.monto_cancelacion_deuda_alquiler

        # Crear instancia de Liquidaciondetalle para Deuda Pendiente si cumple condiciones
        if deuda_pendiente_mas_reciente > 0:
            tipodeduccion_deuda_pendiente = Tipodeduccion.objects.get(tipo_deduccion_descripcion='Deuda Pendiente')
            liquidacion_detalle = Liquidaciondetalle(
                fk_Liquidaciondetalle_Liquidacionencabezado_id=id_liquidacion_enc,
                fk_Liquidaciondetalle_Tipodeduccion=tipodeduccion_deuda_pendiente,
                detalle_liquidacion_monto=deuda_pendiente_mas_reciente,
                detalle_liquidacion_iva=0.00,
                detalle_liquidacion_irpf=0.00,
                detalle_liquidacion_debe=0.00
            )
            liquidacion_detalle.save()

        # FILAS PLUS   -----------------------------------------------------------------

        # Obtener todas las instancias de Contratoalquilerdeducciones asociadas a la propiedad_contrato_alquiler
        contrato_deducciones = propiedadcontratoalquiler.propiedades_contrato_alquiler.all()

        descripcion_values = []

        # Recorrer las instancias de Contratoalquilerdeducciones
        for contrato_deduccion in contrato_deducciones:
            # Obtener la instancia de Propiedaddeducciones asociada a cada Contratoalquilerdeducciones
            propiedades_deducciones = contrato_deduccion.fk_Contratoalquilerdeducciones_Propiedadeducciones

            # Obtener la instancia de Tipodeduccion asociada a cada Propiedaddeducciones
            tipo_deduccion = propiedades_deducciones.fk_Propiedadeducciones_Tipodeduccion

            # Obtener y agregar la descripción de Tipodeduccion
            descripcion_values.append(tipo_deduccion.tipo_deduccion_descripcion)


        # Ordenar la lista descripcion_values en orden alfabético
        descripcion_valores= sorted(descripcion_values)
        

        valores_editados = []

        for descripcion in descripcion_valores:
            celda2 = descripcion

            celda3 = request.POST.get(f'celda3_{celda2}', '0')  # Asignar '0' si está vacía
            celda4 = request.POST.get(f'celda4_{celda2}', '0')
            celda5 = request.POST.get(f'celda5_{celda2}', '0')

            # Convertir a float solo si no es vacío
            celda3 = float(celda3) if celda3 else 0.0
            celda4 = float(celda4) if celda4 else 0.0
            celda5 = float(celda5) if celda5 else 0.0

          

            

            # Obtener el id_tipo_deduccion correspondiente a la descripción
            tipodeduccion = Tipodeduccion.objects.get(tipo_deduccion_descripcion=celda2)
            id_tipo_deduccion = tipodeduccion.id_tipo_deduccion


            valores_editados.append({
                'id_tipo_deduccion': id_tipo_deduccion,
                'celda3': celda3,
                'celda4': celda4,
                'celda5': celda5,
               
            })


        #  iterar sobre los valores en valores_editados, crear una instancia de Liquidaciondetalle para cada valor 
        for valor in valores_editados:
            id_tipo_deduccion = valor['id_tipo_deduccion']
            celda3 = valor['celda3']
            celda4 = valor['celda4']
            celda5 = valor['celda5']
           

            liquidacion_detalle = Liquidaciondetalle(
                fk_Liquidaciondetalle_Liquidacionencabezado_id=id_liquidacion_enc,
                fk_Liquidaciondetalle_Tipodeduccion_id=id_tipo_deduccion,
                detalle_liquidacion_monto=celda3,
                detalle_liquidacion_iva=celda4,
                detalle_liquidacion_irpf=celda5,
                
            )
            liquidacion_detalle.save()



    # FILAS AGREGADAS POR EL USUARIO ------------------------------------------------------

            propiedades = Propiedadcontratoalquiler.objects.all()
            valores_celda3 = {}

            for objeto in propiedades:
                # Trabaja con cada "objeto" en el bucle aquí
                propiedades_id = objeto.id_propiedad_contrato_alquiler

                # Construye el nombre del campo para la celda 3
                campo_celda3 = f'celda-agregada3-{propiedades_id}'

                # Obtén el valor de la celda 3 usando el nombre del campo
                valor_celda3 = request.POST.get(campo_celda3)

                # Almacena el valor en un diccionario donde la clave es propiedades_id
                valores_celda3[propiedades_id] = valor_celda3

            # Ahora, tienes los valores de la celda 3 en el diccionario valores_celda3, donde puedes acceder a ellos según el objeto













        #opcion_elegida = request.POST.getlist('celda2[]')
        #valor_celda3 = request.POST.getlist('valorCelda3[]')
        #valor_celda4 = request.POST.getlist('valorCelda4[]')
        #valor_celda5 = request.POST.getlist('valorCelda5[]')



            
        # Procesa los datos como desees
        # for fila in data['filas']:
        #     tablaId = fila.get('tablaId')
        #     opcion = fila.get('opcion')
        #    valor3 = fila.get('valor3')
        #    valor4 = fila.get('valor4')
        #    valor5 = fila.get('valor5')


        #print("opcion :", opcion_elegida)  # Imprime los valores recibidos en el registro de Django
        

        #print("celda4 :", valor_celda4)  # Imprime los valores recibidos en el registro de Django
        #print("celda4 :", valor_celda5)  # Imprime los valores recibidos en el registro de Django
        


        # Aquí fuela lógica del POST que recibe y procesa los datos de las filas
        # Procesa los datos y guárdalos en la base de datos según tus necesidades
        # ...

        # Después de procesar la solicitud POST, redirige a otra vista o devuelve una respuesta JSON con éxito
        return JsonResponse({'message': 'Datos guardados exitosamente'})




 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    


def generate_pdf(request):

       # Obtén los datos del formulario y realiza cualquier procesamiento necesario

    # Crear un objeto de BytesIO para almacenar el PDF en memoria
    buffer = BytesIO()

    # Crear el objeto PDF
    pdf = canvas.Canvas(buffer, pagesize=letter)
    
    # Obtener las dimensiones de la página
    page_width, page_height = letter


    #-----------------------------------------------------------------------------------

    # Ruta relativa a la imagen estática
    logo_path = '/home/ale/MEGA/proyectoMEGA/appMEGA/static/appMEGA/img/logo1.png'

    # Obtener las dimensiones de la imagen del logo
    logo_width, logo_height = 150, 74.09  # Ajusta el ancho y alto según tus necesidades(100 px aprox 1,39cm)

    # Calcular las coordenadas para centrar la imagen en la parte superior de la página
    x = (page_width - logo_width) / 2
    y = page_height - inch - logo_height  # Ajusta la posición vertical según sea necesario (una pulgada (inch) desde el borde superior)

    # Agregar el logo de la empresa en la cabecera, centrado
    pdf.drawImage(logo_path, x, y, width=logo_width, height=logo_height)

    

    #--------------------------------------------------------------------------------------------------

    # Obtén el valor de propiedadcontratoalquiler_id de la URL
    propiedadcontratoalquiler_id = request.GET.get('propiedadcontratoalquiler_id')


    # Obtener LA INSTANCIA de Propiedadcontratoalquiler
    propiedadcontratoalquiler = Propiedadcontratoalquiler.objects.get(pk=propiedadcontratoalquiler_id)

    # Obtener datos de la empresa que alquila la propiedad
    empresa_apellido1 = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_apellido1
    empresa_apellido2 = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_apellido2
    empresa_nombre1= propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_nombre1
    empresa_nombre2= propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_nombre2
    empresa_razonsocial= propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_razon_social
    empresa_telefono= propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_telefono1
    empresa_email= propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Contratos.fk_Contratos_Empresas.empresa_email


    # Crear una lista para almacenar los datos no vacíos de la empresa
    datos_empresa = []

    # Verificar y agregar los datos no vacíos a la lista
    if empresa_apellido1:
        datos_empresa.append(f"Apellido 1: {empresa_apellido1}")

    if empresa_apellido2:
        datos_empresa.append(f"Apellido 2: {empresa_apellido2}")

    if empresa_nombre1:
        datos_empresa.append(f"Nombre 1: {empresa_nombre1}")

    if empresa_nombre2:
        datos_empresa.append(f"Nombre 2: {empresa_nombre2}")

    if empresa_razonsocial:
        datos_empresa.append(f"Razón Social: {empresa_razonsocial}")

    if empresa_telefono:
        datos_empresa.append(f"Teléfono: {empresa_telefono}")

    if empresa_email:
        datos_empresa.append(f"Email: {empresa_email}")


    # Generar el texto con los datos en los renglones específicos
    lineas = []

    # Si hay datos en 'datos_empresa', combina Apellido1, Apellido2, Nombre1 y Nombre2 en el Renglón 1
    if datos_empresa:
        nombres_apellidos = [empresa_apellido1, empresa_apellido2, empresa_nombre1, empresa_nombre2]
        nombres_apellidos = [nombre for nombre in nombres_apellidos if nombre]  # Elimina valores vacíos
        linea1 = " ".join(nombres_apellidos)
        lineas.append(linea1)  # Renglón 1: Apellido1 Apellido2 Nombre1 Nombre2

    # Agregar Razón Social, Teléfono y Email en los Renglones restantes
    if empresa_razonsocial:
        lineas.append(empresa_razonsocial)  # Renglón 2: Razón Social
    if empresa_telefono:
        lineas.append(empresa_telefono)  # Renglón 3: Teléfono
    if empresa_email:
        lineas.append(empresa_email)  # Renglón 4: Email

    x_texto = 0  # Ajusta el valor según tus necesidades
    y_texto = 630  # Ajusta el valor según tus necesidades
    
    # Agregar cada elemento de la lista 'lineas' debajo del logo, justificado a la derecha
    for linea in lineas:
        pdf.drawRightString(page_width - x_texto, y_texto, linea)  # Utiliza drawRightString
        x_texto=30
        y_texto -= 15  # Espacio entre los renglones

    #-----------------------------------------------------------------------------------------
    
    # Obtén el valor de fecha_siguiente de la URL
    fecha_siguiente = request.GET.get('fecha_siguiente')
    
    titulo = "Liquidación de Arrendamiento"
    subtitulo = f"Detalle a abonar correspondiente al período: {fecha_siguiente}"


    # Configurar el título y el subtítulo en el PDF
    pdf.setFont("Helvetica-Bold", 14)  # Fuente y tamaño para el título
    pdf.drawString(x_texto, y_texto, titulo)

    # Agregar un salto de línea entre el título y el subtítulo
    y_texto -= 15 # Espacio adicional

    pdf.setFont("Helvetica", 12)  # Fuente y tamaño para el subtítulo
    pdf.drawString(x_texto, y_texto, subtitulo)

    #-----------------------------------------------------------------------------------------

     # Obtén el valor de propiedadcontratoalquiler_id de la URL
    propiedadcontratoalquiler_id = request.GET.get('propiedadcontratoalquiler_id')


    # Obtener LA INSTANCIA de Propiedadcontratoalquiler
    propiedadcontratoalquiler = Propiedadcontratoalquiler.objects.get(pk=propiedadcontratoalquiler_id)
    # Obtener los clientes activos vinculados a esa propiedadcontratoalquiler

    
    clientes_activos = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Clientes.filter(cl_estado='ACTIVO')


    # Crear una lista para almacenar líneas por cliente
    lineas_clientes = []

    # Inicializar la posición vertical
    x_texto =30
    y_texto_inicial = 530  # Ajusta el valor según tus necesidades
    altura_linea = 15  # Ajusta el valor según la altura de línea deseada

    # Agregar una línea por cada cliente activo con sus datos
    for cliente in clientes_activos:
        # Crear una lista para almacenar datos por cliente
        datos_cliente = []

        # Obtener los datos del cliente activo
        apellido1 = cliente.cl_apellido1
        apellido2 = cliente.cl_apellido2
        nombre1 = cliente.cl_nombre1
        nombre2 = cliente.cl_nombre2
        razon_social = cliente.cl_razon_social

        # Verificar y agregar los datos no vacíos a la lista
        if apellido1:
            datos_cliente.append(f"{apellido1}")
        if apellido2:
            datos_cliente.append(f"{apellido2},")
        if nombre1:
            datos_cliente.append(f"{nombre1}")
        if nombre2:
            datos_cliente.append(f"{nombre2}")
        if razon_social:
            datos_cliente.append(f"{razon_social}")

        # Unir los datos del cliente en una línea y agregarlo a la lista de líneas
        linea_cliente = " ".join(datos_cliente)
        lineas_clientes.append(linea_cliente)

       

        pdf.setFont("Helvetica-Oblique", 12)  # Fuente y tamaño para el subtítulo

        # Dibujar la línea del cliente en el PDF
        pdf.drawString(x_texto, y_texto_inicial, linea_cliente)

        # Ajustar la posición vertical para el siguiente cliente
        y_texto_inicial -= altura_linea

        #-----------------

    calle_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.prop_calle
    numero_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.prop_numero
    piso_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.prop_piso
    departamento_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.prop_departamento
    codigo_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Poblaciones.codigo_postal
    poblacion_propiedad = propiedadcontratoalquiler.fk_Propiedadcontratoalquiler_Propiedades.fk_Propiedades_Poblaciones.poblacion_descripcion

    # Crear una lista para almacenar domicilio
    domicilio = []

    # Verificar y agregar los datos no vacíos a la lista
    if calle_propiedad:
        domicilio.append(f"{calle_propiedad}")
    if numero_propiedad:
        domicilio.append(f"{numero_propiedad}")
    if piso_propiedad:
        domicilio.append(f"{piso_propiedad}")
    if departamento_propiedad:
        domicilio.append(f"{departamento_propiedad}")

    domicilio_propiedad = " ".join(domicilio)

    # Calcular la altura total de las líneas de clientes
    altura_total_clientes = len(lineas_clientes) * altura_linea

    # Calcular la posición vertical del domicilio
    y_texto_domicilio = y_texto_inicial - altura_total_clientes  
    # Dibujar el domicilio de la propiedad en el PDF
    pdf.drawString(30, y_texto_domicilio, domicilio_propiedad)

    # Crear una lista para almacenar población
    poblacion = []

    # Verificar y agregar los datos no vacíos a la lista
    if codigo_propiedad:
        poblacion.append(f"({codigo_propiedad})")
    if poblacion_propiedad:
        poblacion.append(f"{poblacion_propiedad}")

    poblacion_propiedad = " ".join(poblacion)

    # Dibujar la línea del cliente en el PDF
    pdf.drawString(30, 485, poblacion_propiedad)

    #-----------------------------------------------------------------------------------------

    encabezados = ["CONCEPTO", "MONTO", "IVA", "IRPF", "DEBE"]
    datos_tabla = [encabezados]
    ultimo_encabezado = Liquidacionencabezado.objects.filter(fk_Liquidacionenc_Propiedadcontratoalquiler=propiedadcontratoalquiler_id
).latest('id_liquidacion_enc')


    
    detalles_de_liquidacion = Liquidaciondetalle.objects.filter(fk_Liquidaciondetalle_Liquidacionencabezado=ultimo_encabezado)

    for detalle in detalles_de_liquidacion:
        fila = [
            detalle.fk_Liquidaciondetalle_Tipodeduccion.tipo_deduccion_descripcion,
            str(detalle.detalle_liquidacion_monto),
            str(detalle.detalle_liquidacion_iva),
            str(detalle.detalle_liquidacion_irpf),
            str(detalle.detalle_liquidacion_debe)
        ]
        datos_tabla.append(fila)

    # Definir los anchos relativos de las columnas
    anchos_columnas = [100, 100, 100, 100, 100]  # Valores en puntos

    # Crear una tabla a partir de los encabezados y los datos
    tabla_data = datos_tabla
    tabla = Table(tabla_data, colWidths=anchos_columnas)

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#84B0CA')), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Color de texto en el encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación de texto en el centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente y negrita para el encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 14),  # Espaciado inferior en el encabezado
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#FFFFFF')),  # Color de fondo para filas impares (blanco)
        ('BACKGROUND', (0, 2), (-1, -1), colors.HexColor('#F0F0F0')),  # Color de fondo para filas pares (gris claro)
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#f2f2f2'))  # Líneas de cuadrícula
    ])

    tabla.setStyle(style)

    # Definir la posición donde deseas colocar la tabla en el PDF
    x = 50  # Coordenada X
    y = 340  # Coordenada Y

    # Coloca la tabla en la posición deseada
    tabla.wrapOn(pdf, 0, 0)
    tabla.drawOn(pdf, x, y)


    # Crea una lista para almacenar los elementos del PDF
    elements = []
    elements.append(tabla)

    #-----------------------------------------------------------------------------------------------------

    data = json.loads(request.body.decode('utf-8'))
            # Aquí data contendrá tu objeto JSON enviado desde JavaScript

    for fila in data['filas']:
        tablaId = fila.get('tablaId')
        opcion = fila.get('opcion')
        valor3 = fila.get('valor3')
        valor4 = fila.get('valor4')
        valor5 = fila.get('valor5')
        # Realiza las operaciones que necesites con estos valores

    print("Valores recibidos:", data)



    #-----------------------------------------------------------------------------------------------------    
  

     # Obtén el valor de mi_input_hidden_dinamico de la solicitud GET
    mi_input_hidden_dinamico = request.GET.get('mi_input_hidden_dinamico', '')

    # Configura la posición x para alinear el texto "Total a pagar" a la derecha con un margen de 30px
    x_texto = 500  # Ajusta este valor según tus necesidades

    # Construye el contenido del PDF
    total_pdf = f'Total a pagar: {mi_input_hidden_dinamico}'

    # Crear una respuesta HTTP con el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="mi_pdf.pdf"'

    # Crear el documento PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    story = []

    # Configurar el título y el subtítulo en el PDF
    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica-Bold", 14)  # Fuente y tamaño para el título
    pdf.drawString(x_texto, 750, "Título del PDF")  # Ejemplo de título
    pdf.setFont("Helvetica", 12)  # Fuente y tamaño para el contenido
    pdf.drawString(x_texto, 730, total_pdf)  # Posición ajustada para el texto







    #-----------------------------------------------------------------------------------------------------    
  
    # Configurar la fuente y el tamaño del texto
    pdf.setFont("Helvetica-Oblique", 11)

    # Definir el texto completo
    texto = '''      IMPORTANTE: 
    * Recuerde informar sus pagos enviando el comprobante de transferencia por mail o WhatsApp.
    * Los pagos son del 01 al 5 de cada mes, sin excepción. 
    * Tenga presente que pasado los primeros 6 meses del contrato de alquiler, toda avería que 
      se produzca en la propiedad por uso, corre a cuenta y cargo del inquilino.
    * UNICA CUENTA BANCARIA HABILITADA:  Banco CAJAMAR - CAJA RURAL 
      Cuenta: ES42 3058 4510 7127 2001 0486 / Beneficiario: MEGA FOREVER SL 
    '''

    # Alinear el texto como desees y establecer la posición de inicio de la caja de texto
    x_texto_inicio = 30
    y_texto_inicio = 250  # Ajustar la posición vertical según sea necesario

    # Ancho deseado para la caja de texto (ajustar según sea necesario)
    ancho_texto_deseado = 300

    # Dividir el texto en líneas y dibujarlas una por una
    lineas = texto.split('\n')
    for linea in lineas:
        pdf.drawString(x_texto_inicio, y_texto_inicio, linea[:500])
        y_texto_inicio -= 15  # Ajustar el espacio vertical entre líneas


    
    # Finalizar el PDF
    pdf.showPage()
    pdf.save()

    # Posiciona el puntero del búfer al inicio
    buffer.seek(0)

    # Configurar la respuesta para mostrar el PDF en una ventana emergente
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ejemplo.pdf"'

    return response