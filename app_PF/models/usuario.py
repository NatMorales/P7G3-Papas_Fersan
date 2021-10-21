from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class userManager(BaseUserManager):
    def crear_usuario(self,nombreusuario, contra=None):
        if not nombreusuario:
            raise ValueError ("El usuario debe tener un nombre")
        usuario = self.model(nombreusuario=nombreusuario)
        usuario.set_contra(contra)
        usuario.save(using=self._db)
        return usuario
    
    def crear_superusuario(self,nombreusuario,contra):
        usuario = self.crear_usuario(
            nombreusuario=nombreusuario,
            contra=contra,
        )
        usuario_is_admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    nombreusuario = models.CharField('nombreusuario', max_length = 15, unique=True)
    contra = models.CharField('Contraseña', max_length=256)
    nombre = models.CharField('Nombre',max_length=30)
    correo = models.EmailField('Correo', max_length=100)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.contra = make_password (self.contra,some_salt)
        super().save(**kwargs) 

    objects = UserManager()
    USERNAME_FIELD = 'nombreusuario'

