from django.urls import path
from django.views.generic import TemplateView
from .views import (
    prueba1, CreatePersonajeView, ListPersonajeView,
    PersonajeDetail, PersonajeUpdateView, pull_data_marvel)



app_name = "personajes"

urlpatterns = [
    path("", prueba1, name="prueba"),
    path("get-datos", pull_data_marvel, name="datos"),
    path("crear-personaje", CreatePersonajeView.as_view(), name="crear-personaje"),
    path("creado/", TemplateView.as_view(template_name="personajes/creado.html"), name="creado"),
    path("list-personajes/", ListPersonajeView.as_view(), name="list"),
    path("detail-personajes/<int:pk>", PersonajeDetail.as_view(), name="detail"),
    path("update-personaje/<int:pk>", PersonajeUpdateView.as_view(), name="update"),
]
