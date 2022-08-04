from django.db import models
# Los modelos se usan para capturar la informacion que sera ingresada

class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100, verbose_name="Titulo")
    imagen= models.ImageField(upload_to="imagenes/", null=True, verbose_name="Imagen")
    descripcion= models.TextField(null=True, verbose_name="Descripcion")

    def __str__(self): #funcion para mostrar los libros y no el object
        return self.titulo 
    
    def delete(self, usign=None, keep_parents=False): #funcion para borrar imagen del visual cuando borramos en el django admin
        self.imagen.delete()
        super().delete()
    




