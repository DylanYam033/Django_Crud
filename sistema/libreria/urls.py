from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

#urls propias de la app, por cada view hay una url que contiene la ruta donde esta el html y si no hay se pone solo el nombre en cuestion
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crear, name="crear"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"), #le pasamos el id del libro a eliminar 
    path("libros/editar/<int:id>", views.editar, name="editar"), #le pasamos el id del libro a editar en una nueva pagina

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #NECESARIO PARA MOSTRAR IMAGENES EN EL CRUD


