from django.db import models

class Data_User(models.Model):
	
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, null = True)
    apellidos = models.CharField(max_length=50, null = True)
    correo = models.CharField(max_length=50, null = True)
    ciudad = models.CharField(max_length=50, null = True)
    
    def __str__(self):
        txt = "{0} - {1} {2} ({3})"
        return txt.format(self.id_usuario,self.nombres,self.apellidos,self.correo)

# Create your models here.