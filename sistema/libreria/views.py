from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Libro #IMPORTO EL MODELO DE LIBRO 
from .forms import LibroForm #IMPORTAMOS EL FORMULARIO PARA SER USADO EN LA VISTA DE CREAR

def inicio(request):
    return render (request, "paginas/inicio.html")  

def nosotros(request):
    return render (request, "paginas/nosotros.html") 

def libros(request):
    libros= Libro.objects.all() #traemos la informacion del modelo y se almacena en libros para luego ser usada en el html de index
    return render (request, "libros/index.html", {"libros": libros}) #defino la ruta donde esta la template y le paso una variable que guarda el queryset del modelo

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) #almacenamos en la variable los datos del formulario con lo que va y luego con la informacion ingresada
    #usamos request.FILES para recepcionar la informacion del formulario ingresada para luego ser guardada y agregada 
    if formulario.is_valid():#si el formulario es valido guardamos la informacion que contiene
        formulario.save()
        return redirect("libros") #redireccionamos la informacion a libros que es la variable que usa nuestro index.html para ser mostrada 
    return render (request, "libros/crear.html", {"formulario": formulario}) #le pasamos al html la variable que contiene los datos del formulario

def editar(request, id):
    libro = Libro.objects.get(id=id) #obtenemos el id del libro y lo almacenamos
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST: #Verificamos si el formulario es valido y si hubo un envio de informacion
        formulario.save() #guardamos la nueva informacion
        return redirect("libros") #redirigimos la nueva informacion a libros que esta en index 
    return render (request, "libros/editar.html", {"formulario": formulario}) #le pasamos al html la variable que contiene los datos del formulario

def eliminar(request, id): #recibe un id para saber que libro se esta eliminando
    libro = Libro.objects.get(id=id) #obtenemos el id del libro y lo almacenamos
    libro.delete()
    return redirect ("libros") #nos quedamos en el html de index pero con el libro ya eliminado 
    


    