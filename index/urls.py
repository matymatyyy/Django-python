from django.urls import path
from index import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tienda/",views.tienda, name='tienda'),   
    path("olvidaste/",views.olvidaste, name="olvidaste"),
    path('procesar-formulario/olvidaste', views.olvidaste, name='olvidaste'),
    path('procesar-formulario/', views.procesar_formulario, name='procesar_formulario'),
    path("registrar/", views.registrar, name='registrar'),
    path('procesar-formulario2/', views.procesar_formulario2, name='procesar_formulario2'),
    path("buy/",views.buy, name="buy" ),
    path("info/",views.infomacion, name="info"),
    path("contacto/",views.contacto, name="contacto"),
    path("trabajo/",views.trabajo, name="trabajo"),
    path('procesar_formulario3/', views.procesar_formulario3, name='procesar_formulario3'),
    path("finalizar/",views.finalizar, name="finalizar"),
]
