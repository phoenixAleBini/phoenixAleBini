

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "appOASIS/index.html")


def vender(request):
    return render(request, "appOASIS/index.html")

def comprar(request):
    return render(request, "appOASIS/index.html")

def alquilar(request):
    return render(request, "appOASIS/index.html")

def tramites(request):
    return render(request, "appOASIS/index.html")

def blog(request):
    return render(request, "appOASIS/index.html")


 
def save_Mega_liq_alq(request):
    if request.method == 'POST':
        return HttpResponse()
    


@csrf_exempt
def enviar_email(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        mensaje = request.POST['mensaje']

        # Aquí puedes realizar acciones como enviar un correo electrónico
        # (Este es solo un ejemplo básico, necesitarás ajustarlo según tus necesidades)
        send_mail(
            'Asunto del correo',
            f'Mensaje de {nombre} {apellido}:\n\n{mensaje}\n\nTeléfono: {telefono}',
            'tu@email.com',
            ['destinatario@email.com'],
            fail_silently=False,
        )

        # Redirigir después del envío (puedes ajustar esto según tus necesidades)
        return HttpResponseRedirect('/gracias/')  # Ajusta la URL de redirección
