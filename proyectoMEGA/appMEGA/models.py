from django.db import models

from .choices import paises
from .choices import provincias
from .choices import tipodoc
from .choices import estado
from .choices import tipo_comprobante
from .choices import tipoprop
from .choices import tipo_contrato
from .choices import tipo_cese_contrato
from .choices import tipoempresa
from .choices import yes_no
from .choices import bcos
from .choices import rh_categ
from .choices import pagos

from .choices import deduc_categ
from .choices import servgastos

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save


from django.contrib.admin.views.main import ChangeList

from django.db.models import Case, When
from django.db.models.expressions import Value

from decimal import Decimal, ROUND_HALF_UP





############################################################################

class Paises(models.Model):
    id_pais=models.AutoField(primary_key=True)
    pais_descripcion=models.CharField(max_length=65,choices=paises, verbose_name="País", null=True, blank=True, default="Sin especificar")

    def __str__(self):
        return '%s'%(self.pais_descripcion)
            
    class Meta:
        verbose_name="País"
        verbose_name_plural="Países"
        ordering=['pais_descripcion']
        db_table="PAISES"

############################################################################

class Provincias(models.Model):
    id_provincia=models.AutoField(primary_key=True)
    provincia_descripcion=models.CharField(max_length=65, choices=provincias, verbose_name="Provincia", null=True, blank=True, default="Sin especificar")
    fk_Provincias_Paises=models.ForeignKey(Paises,  on_delete=models.RESTRICT, verbose_name="País", null=True, blank=True, default=1)

    def __str__(self):
        return '%s'%(self.provincia_descripcion)

    class Meta:
        verbose_name="Provincia"
        verbose_name_plural="Provincias"
        ordering=['provincia_descripcion']
        db_table="PROVINCIAS"

#############################################################################


class Poblaciones(models.Model):
    id_poblacion=models.AutoField(primary_key=True)
    poblacion_descripcion=models.CharField(max_length=65, verbose_name="Población")
    codigo_postal=models.CharField(max_length=6, verbose_name="Código Postal") #opto por que sea escrito a pulso y luego en consulta agregar una verificación
    fk_Poblaciones_Provincias=models.ForeignKey(Provincias,  on_delete=models.RESTRICT, verbose_name="Provincia", null=True, blank=True, default=1)
  
    def __str__(self):
        return '(%s): %s '%(self.codigo_postal, self.poblacion_descripcion)
    
    class Meta:
        verbose_name="Población"
        verbose_name_plural="Poblaciones"
        ordering=['poblacion_descripcion']
        db_table="POBLACIONES"






#############################################################################


class Secuenciacomprobante(models.Model):
    tipo_comprobante = models.CharField(max_length=50, choices=tipo_comprobante, verbose_name="Tipo de Comprobante", unique=True)
    ultimo_numero = models.IntegerField(default=1)
    tipo_comprobante_estado = models.CharField(max_length=20, choices=estado, verbose_name="Estado del tipo de Comprobante", default='Sin especificar')

    def __str__(self):
        return self.tipo_comprobante
    

    class Meta:
        verbose_name="Secuencia Comprobante"
        ordering=['tipo_comprobante_estado', 'tipo_comprobante']
        db_table="SecuenciaComprobante"


#############################################################################

class Tipodoc(models.Model):
    id_tipo_doc=models.AutoField(primary_key=True)
    tipo_doc_descripcion=models.CharField(max_length=25, null=True,blank=True, choices=tipodoc, verbose_name="Tipo de Documento")
    tipo_doc_estado=models.CharField(max_length=20, choices=estado, verbose_name="Estado del tipo de Documento", default='0')

    def __str__(self):
        return '%s'%(self.tipo_doc_descripcion)

    class Meta:
        verbose_name="Documento Tipo"
        ordering=['tipo_doc_estado', 'tipo_doc_descripcion']
        db_table="TIPO_DOCUMENTO"

###############################################################################

class Tipoprop(models.Model):
    id_tipo_propiedades=models.AutoField(primary_key=True)
    tipo_prop_descripcion=models.CharField(max_length=25, null=True, blank=True, choices=tipoprop, verbose_name="Tipo de Propiedades")
    tipo_prop_estado=models.CharField(max_length=20, null=True, blank=True,  choices=estado, verbose_name="Estado de la propiedad", default='0')

    def __str__(self):
        return '%s'%(self.tipo_prop_descripcion)

    class Meta:
        verbose_name="Propiedad Tipo"
        ordering=['tipo_prop_estado', 'tipo_prop_descripcion']
        db_table="TIPO_PROPIEDAD"

###############################################################################

class Tipocontrato(models.Model):
    id_tipo_contrato=models.AutoField(primary_key=True)
    tipo_contrato_descripcion=models.CharField(max_length=25, choices=tipo_contrato, verbose_name="Tipo de Contrato")
    tipo_contrato_estado=models.CharField(max_length=20, choices=estado, verbose_name="Estado del tipo de Contrato", default='0')

    def __str__(self):
        return '%s'%(self.tipo_contrato_descripcion)

    class Meta:
        verbose_name="Contrato Tipo"
        ordering=['tipo_contrato_estado', 'tipo_contrato_descripcion']
        db_table="TIPO_CONTRATO"

###############################################################################


class Tipocesecontrato(models.Model):
    id_tipo_cese_contrato=models.AutoField(primary_key=True)
    tipo_cese_contrato_descripcion=models.CharField(max_length=100, null=True, blank=True, choices=tipo_cese_contrato, verbose_name="Tipo Cese de Contrato")
    tipo_cese_contrato_estado=models.CharField(max_length=20, choices=estado, verbose_name="Estado del tipo Contrato", default='0')

    def __str__(self):
        return '%s'%(self.tipo_cese_contrato_descripcion)

    class Meta:
        verbose_name="Cese de Contrato Tipo"
        ordering=['tipo_cese_contrato_estado', 'tipo_cese_contrato_descripcion']
        db_table="TIPO_CESE_CONTRATO"

###############################################################################

class Clientes(models.Model):
    id_clientes=models.AutoField(primary_key=True)
    cl_apellido1=models.CharField(max_length=65, verbose_name="Primer Apellido", null=True, blank=True)
    cl_apellido2=models.CharField(max_length=65, verbose_name="Segundo Apellido", null=True, blank=True)
    cl_nombre1=models.CharField(max_length=65, verbose_name="Primer Nombre", null=True, blank=True)
    cl_nombre2=models.CharField(max_length=65, verbose_name="Segundo Nombre", null=True, blank=True)
    cl_razon_social=models.CharField(max_length=255, verbose_name="Razón Social", null=True, blank=True)
    
    fk_Clientes_Tipodoc=models.ForeignKey(Tipodoc, null=True, blank=True,default=1, on_delete=models.RESTRICT, verbose_name="Tipo de documento")
    cl_documento=models.CharField(max_length=255, verbose_name="Número Documento", null=True, blank=True)

    cl_calle=models.CharField(max_length=255, verbose_name="Calle", null=True, blank=True)
    cl_numero=models.CharField(max_length=255, verbose_name="Número", null=True, blank=True)
    cl_piso=models.CharField(max_length=255, verbose_name="Piso", null=True, blank=True)
    cl_departamento=models.CharField(max_length=255, verbose_name="Departamento", null=True, blank=True)
    fk_Clientes_Poblaciones=models.ForeignKey(Poblaciones, null=True, blank=True, default=1, on_delete=models.RESTRICT, verbose_name="Población")

    cl_telefono1=models.CharField(max_length=65, verbose_name="Teléfono I", null=True, blank=True)
    cl_telefono2=models.CharField(max_length=65, verbose_name="Teléfono II", null=True, blank=True)
    cl_email=models.EmailField(verbose_name="E Mail", null=True, blank=True)

    cl_observaciones=models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True)
    cl_estado=models.CharField(max_length=20, choices=estado, default='ACTIVO', verbose_name="Estado del cliente")

    

    def __str__(self):
        apellido1 = self.cl_apellido1 if self.cl_apellido1 else ''
        apellido2 = self.cl_apellido2 if self.cl_apellido2 else ''
        nombre1 = self.cl_nombre1 if self.cl_nombre1 else ''
        nombre2 = self.cl_nombre2 if self.cl_nombre2 else ''
        razon_social= self.cl_razon_social if self.cl_razon_social else ''
        
        return '%s %s %s %s %s' % (apellido1, apellido2, nombre1, nombre2,razon_social)


    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
        ordering=['cl_apellido1', 'cl_nombre1']
        db_table="CLIENTES"

#############################################################################
    
class Empresas(models.Model):
    id_empresas=models.AutoField(primary_key=True)
    empresa_apellido1=models.CharField(max_length=65, verbose_name="Primer Apellido", null=True, blank=True)
    empresa_apellido2=models.CharField(max_length=65, verbose_name="Segundo Apellido", null=True, blank=True)
    empresa_nombre1=models.CharField(max_length=65, verbose_name="Primer Nombre", null=True, blank=True)
    empresa_nombre2=models.CharField(max_length=65, verbose_name="Segundo Nombre", null=True, blank=True)
    
    empresa_razon_social=models.CharField(max_length=255, verbose_name="Razón Social", null=True, blank=True)
    empresa_tipo=models.CharField(max_length=8, choices=tipoempresa, null=True, blank=True, verbose_name="Tipo Empresa")

    fk_Empresas_Tipodoc=models.ForeignKey(Tipodoc, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Tipo de documento")
    empresa_documento=models.CharField(max_length=255, verbose_name="Número Documento", null=True, blank=True)
    
    
    empresa_calle=models.CharField(max_length=255, verbose_name="Calle", null=True, blank=True)
    empresa_numero=models.CharField(max_length=255, verbose_name="Número", null=True, blank=True)
    empresa_piso=models.CharField(max_length=255, verbose_name="Piso", null=True, blank=True)
    empresa_departamento=models.CharField(max_length=255, verbose_name="Departamento", null=True, blank=True)
    fk_Empresas_Poblaciones=models.ForeignKey(Poblaciones, on_delete=models.RESTRICT, verbose_name="Poblacion", null=True, blank=True, default= 1)

    empresa_telefono1=models.CharField(max_length=65, verbose_name="Teléfono I", null=True, blank=True)
    empresa_telefono2=models.CharField(max_length=65, verbose_name="Teléfono II", null=True, blank=True)
    empresa_email=models.EmailField(verbose_name="E Mail", null=True, blank=True)
    
    empresa_observaciones=models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True)
    empresa_estado=models.CharField(max_length=20, choices=estado, default='0', verbose_name="Estado de la Empresa")
    
   
   

    def __str__(self):
        apellido1 = self.empresa_apellido1 if self.empresa_apellido1 else ''
        apellido2 = self.empresa_apellido2 if self.empresa_apellido2 else ''
        nombre1 = self.empresa_nombre1 if self.empresa_nombre1 else ''
        nombre2 = self.empresa_nombre2 if self.empresa_nombre2 else ''
        razon_social= self.empresa_razon_social if self.empresa_razon_social else ''


        return '%s %s %s %s %s' % (apellido1, apellido2, nombre1, nombre2,razon_social)


    class Meta:
        verbose_name="Empresa - Arrendador"
        verbose_name_plural="Empresa y Arrendadores"
        ordering=['empresa_razon_social', 'empresa_apellido1', 'empresa_nombre1']
        db_table="EMPRESAS"

###################### CONTRATOS HACE REFERENCIA A CONTRATOS VARIOS (NO AQUILER)n#######################

class Contratos(models.Model):    
    id_contrato=models.AutoField(primary_key=True)
    fecha_inicio_contrato=models.DateField(verbose_name="Fecha de inicio Contrato")
    fecha_cese_contrato=models.DateField(verbose_name="Fecha de cese Contrato", null=True, blank=True)
    contratos_estado=models.CharField(max_length=20, null=True, blank=True, choices=estado, verbose_name="Estado del contrato", default='0')
    contratos_observaciones=models.CharField(max_length=255, null=True, blank=True,verbose_name="Observaciones")
    fk_Contratos_Empresas=models.ForeignKey(Empresas, on_delete=models.RESTRICT, default=1, verbose_name="Arrendador")
    fk_Contratos_Tipocontrato=models.ForeignKey(Tipocontrato, default=1, on_delete=models.RESTRICT, verbose_name="Tipo de Contrato")
    fk_Contratos_Tipocesecontrato=models.ForeignKey(Tipocesecontrato, null=True, blank=True, default=1, on_delete=models.RESTRICT, verbose_name="Tipo de cese de Contrato")


    def __str__(self):
        return " %s" %(self.fk_Contratos_Empresas)
 
    class Meta:
        verbose_name="Contratos varios"
        ordering=['contratos_estado', 'fecha_inicio_contrato', 'fecha_cese_contrato']
        db_table="CONTRATOS"

#############################################################################

class Propiedades(models.Model):
    id_propiedades=models.AutoField(primary_key=True)
    protocolo=models.IntegerField(verbose_name="Número Protocolo")
    prop_calle=models.CharField(max_length=255, verbose_name="Calle")
    prop_numero=models.CharField(max_length=255, verbose_name="Número")
    prop_piso=models.CharField(max_length=255, verbose_name="Piso")
    prop_departamento=models.CharField(max_length=255, verbose_name="Departamento")
    fecha_compra=models.DateField(verbose_name="Fecha Compra")
    valor_compra=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor Compra")
    fecha_venta=models.DateField(verbose_name="Fecha Venta", null=True, blank=True)
    valor_venta=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,verbose_name="Valor Venta")
    sup_construida=models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True, verbose_name="Superficie Construída")
    ano_construccion=models.IntegerField(null=True, blank=True,verbose_name="Año Construcción")
    habitaciones=models.IntegerField(null=True, blank=True,verbose_name="Cantidad de Habitaciones")
    banos=models.IntegerField(null=True, blank=True, verbose_name="Cantidad de Baños")
    aseos=models.IntegerField(null=True, blank=True, verbose_name="Cantidad de Aseos")
    cocina=models.CharField(max_length=2, choices=yes_no, verbose_name="Cocina")
    terraza=models.CharField(max_length=2, choices=yes_no, verbose_name="Terraza")
    observaciones=models.CharField(max_length=255, null=True, blank=True, verbose_name="Observaciones") 
    fk_Propiedades_Poblaciones=models.ForeignKey(Poblaciones, on_delete=models.RESTRICT, verbose_name="Población", null=True, blank=True, default= 1)

    fk_Propiedades_Contratos=models.ForeignKey(Contratos,  on_delete=models.RESTRICT, verbose_name="Contrato Administración")   
    fk_Propiedades_Tipoprop=models.ForeignKey(Tipoprop, on_delete=models.RESTRICT, verbose_name="Tipo de propiedad")      

    def __str__(self):
        return '%s %s -%s %s-' %(self.prop_calle, self.prop_numero, self.prop_piso, self.prop_departamento)

    class Meta:
        verbose_name="Propiedad"
        verbose_name_plural="Propiedades"
        ordering=['prop_calle', 'prop_numero', 'prop_piso', 'prop_departamento']
        db_table="PROPIEDADES"

#############################################################################

class Propiedadcontratoalquiler(models.Model):
    id_propiedad_contrato_alquiler=models.AutoField(primary_key=True)
    propiedad_contrato_alquiler_fecha_inicio=models.DateField(verbose_name="Fecha Inicio del Contrato de Alquiler")
    propiedad_contrato_alquiler_fecha_cese=models.DateField(null=True, blank=True, verbose_name="Fecha Cese del Contrato de Alquiler")
    propiedad_contrato_alquiler_duracion=models.IntegerField(verbose_name="Duración del contrato de alquiler")
    propiedad_contrato_alquiler_mensual_origen=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto mensual al inicio Contrato")
    propiedad_contrato_alquiler_fianza_origen=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto inicial de fianza")
    propiedad_contrato_alquiler_valor_garantia=models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Monto de la garantía")
    propiedad_contrato_alquiler_estado=models.CharField(max_length=20, choices=estado, null=True, blank=True, default='0', verbose_name="Estado del Contrato de Alquiler")
    observaciones=models.CharField(max_length=255, null=True, blank=True, verbose_name="Observaciones") 
    fk_Propiedadcontratoalquiler_Propiedades=models.ForeignKey(Propiedades,  on_delete=models.RESTRICT, verbose_name="Propiedad")
    fk_Propiedadcontratoalquiler_Tipocontrato=models.ForeignKey(Tipocontrato, on_delete=models.RESTRICT, verbose_name="Tipo de Contrato")
    fk_Propiedadcontratoalquiler_Tipocesecontrato=models.ForeignKey(Tipocesecontrato, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Tipo de cese de Contrato")
    fk_Propiedadcontratoalquiler_Clientes = models.ManyToManyField(
        Clientes, 
        blank=True, 
        verbose_name="Arrendatarios", 
        related_name="propiedades_contrato_alquiler",
        through='Propiedadcontratoalquiler_INTERMEDIA_Clientes'
    )  
    #donde related hace referencia a relación inversa y through a la tabla intermedia que crea con las claves primarias de los dos modelos relacionados para almacenar los registros que representan la relación de muchos a muchos.

    def __str__(self):
        clientes = self.fk_Propiedadcontratoalquiler_Clientes.all()
        nombres_clientes = ', '.join([str(cliente) for cliente in clientes])
        return f'{self.fk_Propiedadcontratoalquiler_Propiedades} ({nombres_clientes})'

    class Meta:
        verbose_name = "Contrato de Alquiler de la Propiedad"
        db_table="PROPIEDAD_CONTRATO_ALQUILER"

    @staticmethod
    def get_queryset():
        # Personaliza la consulta y el ordenamiento
        return super().get_queryset().annotate(
            cliente_group=Case(
                When(fk_Propiedadcontratoalquiler_Clientes__isnull=False, then='fk_Propiedadcontratoalquiler_Clientes__nombre'),
                default=Value('')  # Si no hay clientes, se utiliza una cadena vacía para el ordenamiento
            )
        ).order_by(
            'fk_Propiedadcontratoalquiler_Propiedades',
            'cliente_group'
        )

        

class Propiedadcontratoalquiler_INTERMEDIA_Clientes(models.Model):
    propiedadcontratoalquiler = models.ForeignKey(Propiedadcontratoalquiler, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)


#############################################################################

class Liquidacionencabezado(models.Model):
    id_liquidacion_enc = models.AutoField(primary_key=True)
    liquidacion_enc_fecha = models.DateField(null=True, verbose_name="Fecha de liquidación")
    fk_Liquidacionenc_Tipocontrato=models.ForeignKey(Tipocontrato, on_delete=models.RESTRICT, verbose_name="Tipo de Contrato")
    fk_Liquidacionenc_Contratos=models.ForeignKey(Contratos, null=True, on_delete=models.RESTRICT, verbose_name="Contratos varios")
    fk_Liquidacionenc_Propiedadcontratoalquiler=models.ForeignKey(Propiedadcontratoalquiler, null=True, on_delete=models.RESTRICT, verbose_name="Contratos de alquiler")

    def __str__(self):
        return ' %s - %s' %(self.liquidacion_enc_fecha, self.fk_Liquidacionenc_Propiedadcontratoalquiler)

    class Meta:
        verbose_name="Encabezado de la liquidación"
        ordering=['liquidacion_enc_fecha']
        db_table="LIQUIDACION_ENCABEZADO"




#############################################################################

class Comprobantesencabezado(models.Model):
    id_comprobantes_enc = models.AutoField(primary_key=True)
    fk_Comprobantesencabezado_Secuenciacomprobante = models.ForeignKey(Secuenciacomprobante, on_delete=models.CASCADE, verbose_name="Tipo de Comprobante", default=1)
    comprobantes_enc_numero = models.IntegerField(blank=True, null=True, editable=False)
    comprobantes_enc_fecha = models.DateField(null=True, verbose_name="Comprobante Fecha")
    fk_Comprobantesencabezado_Empresas = models.ForeignKey(Empresas, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Empresa")
    fk_Comprobantesencabezado_Clientes = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Cliente")
    fk_Comprobantesencabezado_Liquidacionesencabezado = models.ForeignKey(Liquidacionencabezado, on_delete=models.RESTRICT, verbose_name="Encabezado de liquidación")

    def __str__(self):
        return 'N° %s - %s -' % (self.comprobantes_enc_numero, self.comprobantes_enc_fecha)

@receiver(pre_save, sender=Comprobantesencabezado)
def asignar_numero_comprobante(sender, instance, **kwargs):
    if not instance.comprobantes_enc_numero:
        tipo_comprobante = instance.fk_Comprobantesencabezado_Secuenciacomprobante.tipo_comprobante
        secuencia, _ = Secuenciacomprobante.objects.get_or_create(tipo_comprobante=tipo_comprobante)
        instance.comprobantes_enc_numero = secuencia.ultimo_numero
        secuencia.ultimo_numero += 1
        secuencia.save()


    class Meta:
        verbose_name="Encabezado de Comprobantes"
        ordering=['comprobantes_enc_fecha']
        db_table="COMPROBANTE_ENCABEZADO"




#############################################################################

class Tipodeduccion(models.Model):
    id_tipo_deduccion=models.AutoField(primary_key=True)
    tipo_deduccion_descripcion=models.CharField(max_length=30, choices=servgastos,  default='0',verbose_name="Concepto deducción")
    tipo_deduccion_categoria=models.CharField(max_length=25, choices=deduc_categ, default='0', verbose_name="Categoría deducción")

    def __str__(self):
        return '%s'%(self.tipo_deduccion_descripcion)

    class Meta:
        verbose_name="Tipo Gastos & Servicios"
        ordering=['tipo_deduccion_descripcion']
        db_table="TIPO_DEDUCCION"

# vinculado con forms.py para limitar las choices.
#############################################################################

class Liquidaciondetalle(models.Model):
    id_detalle_liquidacion=models.AutoField(primary_key=True)
    fk_Liquidaciondetalle_Liquidacionencabezado=models.ForeignKey(Liquidacionencabezado,  on_delete=models.RESTRICT, verbose_name="Encabezado de liquidación")
    detalle_liquidacion_monto=models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,verbose_name="Monto item liquidado")
    detalle_liquidacion_iva=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, verbose_name="IVA item liquidado")
    detalle_liquidacion_irpf=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, verbose_name="IRPF item liquidado")
    detalle_liquidacion_debe=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, verbose_name="Debe item liquidado")
    fk_Liquidaciondetalle_Tipodeduccion=models.ForeignKey(Tipodeduccion, default=1, on_delete=models.RESTRICT, verbose_name="Detalles de liquidación")



    def __str__(self):
        return '%s'%(self.detalle_liquidacion_monto)

    class Meta:
        verbose_name="Detalle de items liquidados"
        ordering=['detalle_liquidacion_monto']
        db_table="LIQUIDACION_DETALLE"

#############################################################################

class Comprobantedetalle(models.Model):
    id_comprobante_detalle=models.AutoField(primary_key=True)
    comprobante_detalle_importe=models.PositiveIntegerField(default=0, verbose_name="Importe")
    comprobante_detalle_iva=models.PositiveIntegerField(default=0,null=True, blank=True, verbose_name="IVA")
    comprobante_detalle_irpf=models.PositiveIntegerField(default=0,null=True, blank=True, verbose_name="irpf")
    fk_Comprobantedetalle_Comprobantesencabezado=models.ForeignKey(Comprobantesencabezado, on_delete=models.RESTRICT, verbose_name="Encabezado de comprobante")
    fk_Comprobantedetalle_Liquidacionencabezado=models.ForeignKey(Liquidacionencabezado, on_delete=models.RESTRICT, verbose_name="Encabezado de liquidación")
    fk_Comprobantedetalle_Liquidaciondetalle=models.ForeignKey(Liquidaciondetalle,  on_delete=models.RESTRICT, verbose_name="Detalle de liquidación")


    def __str__(self):
        return '%s -iva %s -irpf %s'%(self.comprobante_detalle_importe, self.comprobante_detalle_iva, self.comprobante_detalle_irpf)

    class Meta:
        verbose_name="Detalle del comprobante"
        ordering=['comprobante_detalle_importe']
        db_table="COMPROBANTE_DETALLE"

#############################################################################

class Bancos(models.Model):
    id_bancos=models.AutoField(primary_key=True)
    bancos_descripcion=models.CharField(max_length=25, null=True, blank=True, choices=bcos, verbose_name="Bancos")
    bancos_estado=models.CharField(max_length=20, null=True, blank=True, choices=estado, verbose_name="Estado del banco", default='0')

    def __str__(self):
        return '%s (%s)'%(self.bancos_estado, self.bancos_descripcion)

    class Meta:
        verbose_name="Banco"
        verbose_name_plural="Bancos"
        ordering=['bancos_estado', 'bancos_descripcion']
        db_table="BANCOS"


#############################################################################

class Empleados(models.Model):
    id_empleados=models.AutoField(primary_key=True)
    empleado_legajo=models.IntegerField(verbose_name="Número Legajo", null=True, blank=True)
    empleado_documento=models.CharField(max_length=255, verbose_name="Documento", null=True, blank=True)
    empleado_cuil=models.CharField(max_length=255, verbose_name="Cuil")
    empleado_fecha_alta=models.DateField(null=True, blank=True, verbose_name="Fecha Alta de Empleado")
    empleado_fecha_baja=models.DateField(null=True, blank=True, verbose_name="Fecha Baja de Empleado")
    empleado_fecha_nac=models.DateField(null=True, blank=True, verbose_name="Fecha Nacimiento Emleado")
    empleado_apellido=models.CharField(max_length=255, verbose_name="Apellido", null=True, blank=True )
    empleado_nombre=models.CharField(max_length=255, verbose_name="Nombre", null=True, blank=True)
    empleado_calle=models.CharField(max_length=255, null=True,blank=True, verbose_name="Calle")
    empleado_numero=models.CharField(max_length=255, null=True, blank=True,  verbose_name="Número")
    empleado_piso=models.CharField(max_length=255, null=True, blank=True, verbose_name="Piso")
    empleado_departamento=models.CharField(max_length=255, null=True,blank=True,  verbose_name="Departamento")
    empleado_telefono1=models.CharField(max_length=65, verbose_name="Teléfono I", null=True, blank=True)
    empleado_telefono2=models.CharField(max_length=65, verbose_name="Teléfono II", null=True, blank=True)
    empleado_fax=models.CharField(max_length=65, verbose_name="Fax", null=True, blank=True)
    empleado_email=models.EmailField(verbose_name="E Mail", null=True, blank=True)
    empleado_categoria=models.CharField(max_length=25, null=True, blank=True, choices=rh_categ,verbose_name="Categoría Empleado")
    empleado_estado=models.CharField(max_length=20, choices=estado, default='0', verbose_name="Estado del Empleado")  
    empleado_observaciones=models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True )
    fk_Empleados_Poblaciones=models.ForeignKey(Poblaciones, null=True, blank=True, default=1, on_delete=models.RESTRICT,verbose_name="Población")

    fk_Empleados_Empresas=models.ForeignKey(Empresas, null=True, blank=True,default=1,  on_delete=models.RESTRICT, verbose_name="Empresa")
    fk_Empleados_Tipodoc=models.ForeignKey(Tipodoc, null=True, blank=True, default=1, on_delete=models.RESTRICT, verbose_name="Tipo de documento")


    def __str__(self):
        return '%s, %s (%s)'%(self.empleado_apellido, self.empleado_nombre, self.empleado_estado)

    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Empleados"
        ordering=['empleado_estado', 'empleado_apellido', 'empleado_nombre' ]
        db_table="EMPLEADOS"


#############################################################################

class Tipopagos(models.Model):
    id_tipo_pagos=models.AutoField(primary_key=True)
    tipo_pagos_descripcion=models.CharField(max_length=25, null=True, blank=True, choices=pagos, verbose_name="Forma de pago")
    tipo_pagos_estado=models.CharField(max_length=20, choices=estado, verbose_name="Estado Tipo de Pagos", default='0')

    def __str__(self):
        return '%s'%(self.tipo_pagos_descripcion)

    class Meta:
        verbose_name="Tipo de pago"
        ordering=['tipo_pagos_estado', 'tipo_pagos_descripcion']
        db_table="TIPO_PAGOS"


#############################################################################

class Pagos(models.Model):
    id_pagos=models.AutoField(primary_key=True)
    pago_numero=models.IntegerField(verbose_name="Número de Pago", default='0')
    pago_fecha=models.DateField(null=True, verbose_name="Fecha Pago")
    pago_importe=models.PositiveIntegerField(verbose_name="Importe Pago", default='0')
    fk_Pagos_Liquidacionencabezado=models.ForeignKey (Liquidacionencabezado, on_delete=models.RESTRICT, verbose_name="Encabezado de liquidación")
    fk_Pagos_Comprobantesencabezado=models.ForeignKey(Comprobantesencabezado, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Encabezado de comprobante")
    fk_Pagos_Empresas=models.ForeignKey(Empresas, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Empresa")
    fk_Pagos_Secuenciacomprobante=models.ForeignKey(Secuenciacomprobante, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Tipo de comprobante")
    fk_Pagos_Tipopagos=models.ForeignKey(Tipopagos, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Tipo de pago")
    fk_Pagos_Bancos=models.ForeignKey(Bancos, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Banco")

    def __str__(self):
        return '-N°%s %s Importe: %s'%(self.pago_numero, self.pago_fecha, self.pago_importe)

    class Meta:
        verbose_name="Pago"
        verbose_name_plural="Pagos"
        ordering=['pago_numero']
        db_table="PAGOS"

#############################################################################


class Propiedadcontratogarante(models.Model):
    id_garante=models.AutoField(primary_key=True)
    garante=models.CharField(max_length=25, choices=yes_no, default='N', verbose_name="Garante")
    garante_observaciones=models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True)    
    fk_Propiedadcontratogarante_Propiedadcontratoalquiler=models.ForeignKey(Propiedadcontratoalquiler, on_delete=models.RESTRICT, verbose_name="Contrato de alquiler")
    fk_Propiedadcontratogarante_Clientes=models.ForeignKey(Clientes, on_delete=models.RESTRICT, verbose_name="Cliente")

    def __str__(self):
        return 'Garante: %s'%(self.garante)

    class Meta:
        verbose_name="Garante Alquiler"
        db_table="PROPIEDAD_CONTRATO_GARANTE"
      

#############################################################################

class Propiedadcontratoaumentos(models.Model):
    id_aumentos=models.AutoField(primary_key=True)
    fk_Propiedadcontratoaumentos_Propiedadcontratoalquiler=models.ForeignKey(
        Propiedadcontratoalquiler, 
        on_delete=models.RESTRICT, 
        related_name='propiedadcontratoaumentos_set',  # Nombre de la relación inversa
        verbose_name="Contrato de alquiler")
    aumentos_indice=models.DecimalField(max_digits=10, decimal_places=6, default=1, verbose_name="Índice de aumento") 
    aumentos_fianza_actualizada=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fianza actualizada")
    aumentos_mensual_actualizado=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Mensual actualizado")
    aumentos_observaciones=models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True)    
    diferencia_fianza=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Diferencia en la fianza", default=0)
    aumento_mes_mismo = models.IntegerField(verbose_name="Aumento en el mes siguiente", default=1)

    
    def __str__(self):
        return 'Índice: %s' %(self.aumentos_indice)

    class Meta:
        verbose_name="Actualización contrato alquiler"
        verbose_name_plural= "Actualizaciones del contrato de alquiler"
        ordering=['aumentos_indice']
        db_table="PROPIEDAD_CONTRATO_AUMENTOS"



# Las siguientes funciones INTRODUCEn UNA SEÑAL 
# Requiere  también intervención en signals.py y apps.py

@receiver(pre_save, sender=Propiedadcontratoaumentos)
def actualizar_mensual_actualizado(sender, instance, **kwargs):
    if instance.pk:  # Verificar si es una instancia existente
        old_instance = Propiedadcontratoaumentos.objects.get(pk=instance.pk)
        if instance.aumentos_indice != old_instance.aumentos_indice:
            # El valor de aumentos_indice ha cambiado
            instance.aumentos_mensual_actualizado *= instance.aumentos_indice
            instance.aumentos_fianza_actualizada *= instance.aumentos_indice
            instance.diferencia_fianza = instance.aumentos_fianza_actualizada - old_instance.aumentos_fianza_actualizada

            # Redondear los valores a números enteros
            #instance.aumentos_mensual_actualizado = round(instance.aumentos_mensual_actualizado)
            #instance.aumentos_fianza_actualizada = round(instance.aumentos_fianza_actualizada)
            #instance.diferencia_fianza = round(instance.diferencia_fianza)

            # Establecer aumentos_indice en 1
            instance.aumentos_indice = 1



#############################################################################

class Proveedores(models.Model):
    id_proveedores=models.AutoField(primary_key=True)
    proveedores_descripcion=models.CharField(max_length=255, null=True, verbose_name="Proveedores")
    
    proveedores_calle=models.CharField(max_length=255, null=True,verbose_name="Calle")
    proveedores_numero=models.CharField(max_length=255, null=True, verbose_name="Número")
    proveedores_piso=models.CharField(max_length=255, null=True, verbose_name="Piso")
    proveedores_departamento=models.CharField(max_length=255, null=True, verbose_name="Departamento")
    proveedores_telefono1=models.CharField(max_length=65, verbose_name="Teléfono I", null=True)
    proveedores_telefono2=models.CharField(max_length=65, verbose_name="Teléfono II", null=True)
    proveedores_email=models.EmailField(verbose_name="E Mail", null=True)
    proveedores_estado=models.CharField(max_length=20, null=True, choices=estado, default='0', verbose_name="Estado Proveedores")  
    fk_Proveedores_Poblaciones=models.ForeignKey(Poblaciones, on_delete=models.RESTRICT, verbose_name="Población", null=True, blank=True, default= 1)


    def __str__(self):
        return '%s'%(self.proveedores_descripcion)

    class Meta:
        verbose_name="Proveedores"
        ordering=['proveedores_descripcion']
        db_table="PROVEEDORES"

#############################################################################

class Propiedadeducciones(models.Model):
    id_servicios=models.AutoField(primary_key=True)
    fk_Propiedadeducciones_Propiedades=models.ForeignKey(Propiedades, on_delete=models.RESTRICT, verbose_name="Propiedad")
    fk_Propiedadeducciones_Tipodeduccion=models.ForeignKey (Tipodeduccion, on_delete=models.RESTRICT, verbose_name="Tipo de deducción")
    servicios_medidor=models.CharField(max_length=255, null=True, blank=True, verbose_name="Medidor servicio")    
    servicios_iban=models.CharField(max_length=255, null=True, blank=True,verbose_name="Código IBAN-pago serv-")  
    fk_Propiedadeducciones_Proveedores=models.ForeignKey(Proveedores, on_delete=models.RESTRICT, verbose_name="Proveedor", null=True, blank=True)
    servicios_pago_propiedad=models.CharField(max_length=2, choices=yes_no, default='NO', verbose_name="Corresponde a la propiedad")
    servicios_observaciones=models.CharField(max_length=255, null=True, blank=True, verbose_name="Observaciones")  
        

    def __str__(self):
        return '(%s) %s -PROPIEDAD: %s'%(self.fk_Propiedadeducciones_Propiedades, self.fk_Propiedadeducciones_Tipodeduccion, self.servicios_pago_propiedad)

    class Meta:
        verbose_name="Deducciones de la Propiedad"
        db_table="PROPIEDAD_DEDUCCIONES"
        ordering=['fk_Propiedadeducciones_Propiedades', 'servicios_pago_propiedad']
      

#############################################################################

class Contratoalquilerdeducciones(models.Model):
    id_contrato_deducciones=models.AutoField(primary_key=True)
    fk_Contratoalquilerdeducciones_Propiedadcontratoalquiler=models.ForeignKey(
        Propiedadcontratoalquiler, 
        on_delete=models.RESTRICT, 
        related_name="propiedades_contrato_alquiler",
        verbose_name="Contrato de Alquiler de la Propiedad")
    fk_Contratoalquilerdeducciones_Propiedadeducciones=models.ForeignKey(Propiedadeducciones, on_delete=models.RESTRICT, verbose_name="Deducciones que abona la propiedad")
    servicios_pago_inquilinos=models.CharField(max_length=2, choices=yes_no, default='N', verbose_name="Corresponde al inquilino")

    def __str__(self):
        return '%s, ARRENDATARIO: %s-'%(self.fk_Contratoalquilerdeducciones_Propiedadeducciones, self.servicios_pago_inquilinos)

    class Meta:
        verbose_name="Deducciones del Contrato de Alquiler"
        ordering=['fk_Contratoalquilerdeducciones_Propiedadcontratoalquiler', 'servicios_pago_inquilinos']
        db_table="DEDUCCIONES CONTRATO ALQUILER"


#############################################################################

class Deudacontratoalquiler(models.Model):
    id_deuda_alquiler=models.AutoField(primary_key=True)
    fecha_origen_deuda_alquiler=models.DateField(verbose_name="Fecha de origen de la deuda")
    monto_deuda_alquiler= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto original de la deuda", default=0)
    fk_Deudacontratoalquiler_Propiedadcontratoalquiler=models.ForeignKey(
        Propiedadcontratoalquiler, 
        on_delete=models.RESTRICT, 
        related_name='deudacontratoalquiler_set',
        verbose_name="Contrato de alquiler que contrae deuda")

    def __str__(self):
        return '%s: %s - %s'%(self.fk_Deudacontratoalquiler_Propiedadcontratoalquiler, self.monto_deuda_alquiler, self.fecha_origen_deuda_alquiler)

    class Meta:
        verbose_name="Deuda contraída por el arrendatario"
        ordering=['fk_Deudacontratoalquiler_Propiedadcontratoalquiler', 'fecha_origen_deuda_alquiler']
        db_table="DEUDA CONTRAÍDA POR EL ARRENDATARIO"

############################################################################

class Cancelaciondeudacontratoalquiler(models.Model):
    id_cancelacion_deuda_alquiler = models.AutoField(primary_key=True)
    fecha_cancelacion_deuda_alquiler = models.DateField(verbose_name="Fecha de cancelación de deuda")
    monto_cancelacion_deuda_alquiler = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto de cancelación de deuda", default=0)
    cancelacion_observaciones = models.CharField(max_length=255, verbose_name="Observaciones", null=True, blank=True)
    deudapendiente = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Deuda pendiente", default=0, editable=False)
    fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler = models.ForeignKey(
        Deudacontratoalquiler, 
        on_delete=models.RESTRICT, 
        related_name='cancelaciondeudacontratoalquiler_set',
        verbose_name="Cancelación de deuda del contrato de alquiler"
    )

    def _calculate_deudapendiente(self):
        # Guardar la instancia relacionada
        self.fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler.save()

        # Calcular la diferencia utilizando los montos de las instancias guardadas
        diferencia = self.fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler.monto_deuda_alquiler - self.monto_cancelacion_deuda_alquiler
        self.deudapendiente = 0 if diferencia == 0 else diferencia

    def save(self, *args, **kwargs):
        self._calculate_deudapendiente()
        super().save(*args, **kwargs)

    def __str__(self):
        deuda_pendiente_str = str(self.deudapendiente) if self.deudapendiente != 0 else "0"
        return '%s / %s' % (self.fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler, deuda_pendiente_str)


    class Meta:
        verbose_name = "Cancelación de deuda del arrendatario"
        ordering = ['fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler']
        db_table = "CANCELACIÓN DE DEUDA DEL ARRENDATARIO"


    @receiver(post_save, sender=Deudacontratoalquiler)
    def create_cancelacion_deuda_contrato_alquiler(sender, instance, created, **kwargs):
        if created and instance.monto_deuda_alquiler != 0:
            cancelacion = Cancelaciondeudacontratoalquiler.objects.create(
                fecha_cancelacion_deuda_alquiler=instance.fecha_origen_deuda_alquiler,
                monto_cancelacion_deuda_alquiler=instance.monto_deuda_alquiler,
                fk_Cancelaciondeudacontratoalquiler_Deudacontratoalquiler=instance
            )

        # Registro de la señal
    post_save.connect(create_cancelacion_deuda_contrato_alquiler, sender=Deudacontratoalquiler)
