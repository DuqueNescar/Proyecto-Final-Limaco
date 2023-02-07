from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="Registro"),
    path('registrarcurso',views.registrarcurso),
    path('edicioncurso/<codigo>',views.edicioncurso),
    path('editarcurso/',views.editarcurso),
    path('eliminarcurso/<codigo>',views.eliminarcurso),
    path('registro1',views.home1, name="Registro1"),
    path('registrarcurso1',views.registrarcurso1),
    path('edicioncurso1/<codigo1>',views.edicioncurso1),
    path('editarcurso1/',views.editarcurso1),
    path('eliminarcurso1/<codigo1>',views.eliminarcurso1),
    path('registro2',views.home2, name="Registro2"),
    path('registrarcurso2',views.registrarcurso2),
    path('edicioncurso2/<codigo2>',views.edicioncurso2),
    path('editarcurso2/',views.editarcurso2),
    path('eliminarcurso2/<codigo2>',views.eliminarcurso2),
]