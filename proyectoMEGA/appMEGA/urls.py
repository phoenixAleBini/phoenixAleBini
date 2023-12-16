from django.urls import path
from . import views


from .views import obtener_diferencia_fianza



urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('indexadmin/', views.indexadmin, name='indexadmin'),
    path('facturas/', views.facturas, name='facturas'),
    path('card_liquidacion/', views.card_liquidacion, name='card_liquidacion'),
    path('propiedadcontratoaumentos/<int:pk>/', views.propiedadcontratoaumentos_detail, name='propiedadcontratoaumentos_detail'),
    path('liquidMF/', views.liquidMF, name='liquidMF'),
    path('save_Mega_liq_alq/',views.save_Mega_liq_alq, name="save_Mega_liq_alq"),
    path('propiedadcontratoalquiler/<int:id_propiedad_contrato_alquiler>/diferencia_fianza/', obtener_diferencia_fianza, name='obtener_diferencia_fianza'),
    path('generar_pdf/', views.generate_pdf, name='generar_pdf'),
   
   
# El parámetro <int:pk> captura el ID de la instancia de Propiedadcontratoaumentos y lo pasa a la vista propiedadcontratoaumentos_detail.


]




