from django.contrib import admin
from .models.usuario import Usuario
from .models.cuenta import Cuenta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cuenta)

