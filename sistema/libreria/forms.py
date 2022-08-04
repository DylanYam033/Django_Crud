#Formulario para crear libros

from dataclasses import fields
from django import forms #importamos los formularios que vamos a requerir 
from .models import Libro #generamos un formulario a partir de un modelo 

class LibroForm(forms.ModelForm): #lectura y mapeado de nuestro modelo a partir de formularios
    class Meta:
        model = Libro #modelo del cual sera el formulario
        fields = "__all__" #campos a llenar para crear un libro 

#*IMPORTANTE* creamos forms para crear un modelo a partir de un formulario para luego ser usado
# en la view con la informacion de nuestro modelo original y paso a seguir le pasamos esa
# informacion a nuestro html heredando los campos de nuestro modelo original tales como types y labels

#paso 1: crear este archivo
#paso 2: importar este archivo en views.py 
#paso 3: pasarle a nuestra view de crear la informacion traida del formulario y
#almacenarla en una variable para ser usada en el html y recorrerla con el for 