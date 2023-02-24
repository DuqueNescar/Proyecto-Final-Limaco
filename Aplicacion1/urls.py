from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('base',views.base, name="base"),
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
    

    path('login',views.iniciosesion, name='login'),
    path('register',views.registro, name='SignUp'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editar/", views.editarusuario,name="EditarUsuario" ),
    path('avatar/',views.agregaravatar, name="Avatar"),
    path("sobremi/",views.sobremi, name="Sobremi"),
]