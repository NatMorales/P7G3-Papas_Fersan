from app_PF.models.cuenta import Cuenta
from app_Pf.models.usuario import Usuario
from rest_framework import serializers 
from app_PF.serializers.cuentaSerializer import CuentaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    cuenta = CuentaSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'nombreusuario', 'contra', 'nombre', 'correo','account']
        
    def create (self, validated_data):
        accountData= validated_data.pop('account')
        userInstance = Usuario.objects.create(**validated_data)
        Cuenta.objects.create(user = userInstance,**accountData)
        return userInstance
    
    def to_representation(self, obj):
        usuario = Usuario.objects.get(user = obj.id)
        cuenta = Cuenta.objects.get(user = obj.id)
        return{
                'id':user.id,
                'username':user.username,
                'name': user.name,
                'email':user.email,
                'account':{
                    'id':account.id,
                    'balance':account.balance,
                    'lastChangeDate':account.lastChangeDate,                    
                    'isActive': account.isActive
                }
        }
     