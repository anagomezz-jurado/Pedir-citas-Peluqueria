"""
URL configuration for programacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("citas", views.lista, name="lista"),
    path("borrar_cita",views.borrar_cita, name="borrar_cita"),
    path("anadir_cita",views.anadir_cita, name="anadir_cita"),
    path("mostrar_dependienta",views.mostrar_dependienta, name="mostrar_dependienta"),
    path("lista_clientes", views.lista_clientes, name="lista_clientes"),
    path('enviar_datos/', views.tu_vista, name='nombre_de_la_vista'),

]