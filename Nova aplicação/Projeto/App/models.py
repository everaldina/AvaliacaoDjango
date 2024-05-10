from django.db import models

# Create your models here.
class Cursos (models.Model): 
    campo = models.CharField(max_length=200) 
    campo = models.DateTimeField(auto_now_add=True) 
    def __str__ (self): 
        return self.campo