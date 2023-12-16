from django import template

register = template.Library()

@register.filter
def format_date(date):
    return date.strftime("%Y-%m")

# para poder comparar  en liquidMF dos fechas. No reconoce fecha_inicio correctamente den mes y dia


