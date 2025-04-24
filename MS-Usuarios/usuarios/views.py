from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TiposUsuarios, Usuarios
from .serializers import TiposUsuariosSerializer, UsuariosSerializer
from .querysets import ListarUsuarios


class TiposUsuariosView(APIView):
    """
    Vista para manejar operaciones CRUD sobre TiposUsuarios.
    """

    def get(self, request, pk=None):
        """
        Obtener un tipo de usuario por ID o listar todos los tipos de usuarios.
        """
        if pk:
            try:
                tipo_usuario = TiposUsuarios.objects.get(id_tipo_usuario=pk)
                serializer = TiposUsuariosSerializer(tipo_usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TiposUsuarios.DoesNotExist:
                return Response({"error": "Tipo de usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tipos_usuarios = TiposUsuarios.objects.all()
            serializer = TiposUsuariosSerializer(tipos_usuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Crear un nuevo tipo de usuario.
        """
        serializer = TiposUsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Actualizar un tipo de usuario existente.
        """
        try:
            tipo_usuario = TiposUsuarios.objects.get(id_tipo_usuario=pk)
        except TiposUsuarios.DoesNotExist:
            return Response({"error": "Tipo de usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TiposUsuariosSerializer(tipo_usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Eliminar un tipo de usuario.
        """
        try:
            tipo_usuario = TiposUsuarios.objects.get(id_tipo_usuario=pk)
        except TiposUsuarios.DoesNotExist:
            return Response({"error": "Tipo de usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        tipo_usuario.delete()
        return Response({"message": "Tipo de usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)


class UsuariosView(APIView):
    """
    Vista para manejar operaciones CRUD sobre Usuarios.
    """

    def get(self, request, pk=None):
        """
        Obtener un usuario por ID o listar todos los usuarios.
        """
        if pk:
            try:
                usuario = Usuarios.objects.get(id=pk)
                serializer = UsuariosSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Usuarios.DoesNotExist:
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            usuarios = Usuarios.objects.all()
            serializer = UsuariosSerializer(usuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Crear un nuevo usuario.
        """
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Actualizar un usuario existente.
        """
        try:
            usuario = Usuarios.objects.get(id=pk)
        except Usuarios.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Eliminar un usuario.
        """
        try:
            usuario = Usuarios.objects.get(id=pk)
        except Usuarios.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)


class AdministradoresListView(APIView):
    def get(self, request):
        """
        Lista los usuarios administradores.
        """
        # Usar el queryset personalizado
        administradores = Usuarios.objects.consultar_listado_administradores()
        return Response(administradores, status=status.HTTP_200_OK)
