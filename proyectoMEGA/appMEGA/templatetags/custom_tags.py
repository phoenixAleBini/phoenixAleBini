from django import template

register = template.Library()



@register.filter
def tipo_prop_descripcion_valido(value):
    tipos_prop_validos = ['despacho', 'local comercial', 'nave comercial', 'nave agrícola', 'nave industrial', 'nave logística']
    return value in tipos_prop_validos


@register.filter
def calcular_valor(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado = aumento.aumentos_mensual_actualizado * 21 / 100
    else:
        valor_calculado = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado


@register.filter
def calcular_valor2(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado = aumento.aumentos_mensual_actualizado * (-19 )/ 100
    else:
        valor_calculado = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado



@register.filter
def calcular_valor_fianza(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado_fianza = aumento.aumentos_fianza_actualizada * 21 / 100
    else:
        valor_calculado_fianza = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado_fianza


@register.filter
def calcular_valor_fianza2(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado_fianza = aumento.aumentos_fianza_actualizada * (-19 ) / 100
    else:
        valor_calculado_fianza = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado_fianza

@register.filter
def calcular_valor_diffianza(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado_diffianza = aumento.diferencia_fianza * 21 / 100
    else:
        valor_calculado_diffianza = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado_diffianza

@register.filter
def calcular_valor_diffianza2(objeto):
    aumentos = objeto.propiedadcontratoaumentos_set.all()
    if aumentos.exists():
        aumento = aumentos[0]
        valor_calculado_diffianza2 = aumento.diferencia_fianza * (-19 ) / 100
    else:
        valor_calculado_diffianza2 = 0  # Valor predeterminado si no hay aumentos
    return valor_calculado_diffianza2


