from authApp.models.cuenta import Cuenta
from rest_framework import serializers

class CuentaSerializer(serializers.Modelserializer):
    model = Account
    fields = ['balance', 'isActivae', 'lastChangeData']
    