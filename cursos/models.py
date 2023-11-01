from django.db import models

class alumno(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  fechadenacimiento = models.DateField(max_length=100)
  documento = models.CharField(max_length=100)
  domicilio = models.CharField(max_length=100)
  telefono = models.IntegerField(max_length=100)
  genero = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.nombre}, {self.apellido}"



class curso(models.Model):
  diasdelasemana = models.CharField(max_length=100)
  fechadenacimiento = models.DateField(max_length=100)
  fechadenacimiento = models.DateField(max_length=100)
  instructor = models.ForeignKey('instructor', on_delete=models.CASCADE, blank=True, null=True)
  alumno = models.ManyToManyField('alumno', blank=True)

  def __str__(self):
    return self.nombre



class instructor(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  fechadenacimiento = models.DateField(max_length=100)
  documento = models.CharField(max_length=100)
  domicilio = models.CharField(max_length=100)
  telefono = models.IntegerField(max_length=100)
  genero = models.CharField(max_length=100)

  def __str__(self):
    return self.nombre, self.apellido


