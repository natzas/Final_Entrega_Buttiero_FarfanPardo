from django.urls import path
#IMPORTAR LAS VIEWS
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("about" , views.about, name="about" ),
    path("blog" , views.publicacion, name="blog" ),
    path("upload" , views.upload, name= "upload"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view (template_name= "hijo_logout.html"), name="logout"),
    path("buscar_archivo" , views.buscar_archivo),
    path("buscar" , views.buscar),
    path("borrar_publicacion/<int:id>" , views.borrar_publicacion, name="borrar"),
    path("editar/<int:id>" , views.editar , name="editar"),
    path("editar" , views.editar ,name="editar"),
    path("editarperfil" , views.editarperfil , name="editarperfil"),
    path("comentario" , views.comentario , name="comentario"),

]