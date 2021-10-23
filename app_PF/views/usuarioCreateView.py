from rest_framework import status,views
from rest_framework.response import Response 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer

from app_PF.serializer.usuarioSerializer import UsuarioSerializer

class UsuarioCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = { "nombreusuario":request.data["nombreusuario"],
                    "contra":request.data["contra"]}
        tokenSerializer = TokenObtainPairSerializer (data=tokendata)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status= status.HTTP_201_CREATED)