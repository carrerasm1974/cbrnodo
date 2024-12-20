from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Usuario(models.Model): 
    username = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.username
    
class OperacionesCbr(models.Model): 
	tsample = models.FloatField()
	ts = models.DateTimeField()
	reason = models.IntegerField()
      
class MuestrasICbr(models.Model): 
    op_id = models.ForeignKey(OperacionesCbr, on_delete=models.CASCADE, related_name='operacion')
    v0 = models.FloatField(null=True)
    v1 = models.FloatField(null=True)
    v2 = models.FloatField(null=True)
    v3 = models.FloatField(null=True)
    v4 = models.FloatField(null=True)
    v5 = models.FloatField(null=True)
    v6 = models.FloatField(null=True)
    v7 = models.FloatField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class CanalAnalogicoCarga(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    escala = models.CharField(max_length=50)
    unidad = models.CharField(max_length=20)
    valor_actual = models.FloatField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class CanalAnalogicoEH(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],null=False, blank=False)
    escala = models.CharField(max_length=50)
    unidad = models.CharField(max_length=20)
    valor_actual = models.FloatField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class AlarmaCargaSetpoint(models.Model):
    canal = models.ForeignKey(CanalAnalogicoCarga, on_delete=models.CASCADE, related_name='alarmas')
    tipo = models.CharField(max_length=50, choices=[('Alta', 'Alta'), ('Baja', 'Baja')],null=False, blank=False)
    valor = models.FloatField(validators=[MaxValueValidator(30)])
    habilitada = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.tipo} - {self.canal.nombre}"


