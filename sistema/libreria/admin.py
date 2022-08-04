from django.contrib import admin
from .models import Libro

# Register your models here.

class LibrosAdmin(admin.ModelAdmin):
    search_fields = ["titulo"] #agrego un buscador de preguntas al Django admin 

admin.site.register(Libro, LibrosAdmin)


