from django.db import models
from .usuario import Usuario

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,related_name='cuenta', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
