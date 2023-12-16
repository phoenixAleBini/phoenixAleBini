from django.urls import path
from . import views
from .views import enviar_email


urlpatterns = [
    path('index/', views.index, name='index'),
    path('vender/', views.vender, name='vender'),
    path('comprar/', views.comprar, name='comprar'),
    path('alquilar/', views.alquilar, name='alquilar'),
    path('tramites/', views.tramites, name='tramites'),
    path('blog/', views.blog, name='blog'),
    path('enviar_email/', enviar_email, name='enviar_email'),
]


