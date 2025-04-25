from rest_framework import serializers
from usuarios.Models.models import TiposUsuarios, Usuarios

class TiposUsuariosSerializer(serializers.Serializer):
    """
    Serializer para manejar los datos de TiposUsuarios.
    """
    id_tipo_usuario = serializers.IntegerField(read_only=True)
    nombre_tipo = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Método para crear un nuevo tipo de usuario.
        """
        return TiposUsuarios.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Método para actualizar un tipo de usuario existente.
        """
        instance.nombre_tipo = validated_data.get(
            'nombre_tipo', instance.nombre_tipo)
        instance.save()
        return instance


class UsuariosSerializer(serializers.Serializer):
    """
    Serializer para manejar los datos de Usuarios.
    """
    id = serializers.IntegerField(read_only=True)
    identificador_usuario = serializers.CharField(max_length=50)
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    nombre_usuario = serializers.CharField(max_length=50)
    correo = serializers.EmailField(max_length=100)
    rut = serializers.CharField(max_length=20)
    contraseña = serializers.CharField(max_length=255)
    profesion = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    descripcion = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    activo = serializers.BooleanField(default=True)
    id_tipo_usuario = serializers.PrimaryKeyRelatedField(queryset=TiposUsuarios.objects.all())  # Cambio aquí

    def create(self, validated_data):
        """
        Método para crear un nuevo usuario.
        """
        return Usuarios.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Método para actualizar un usuario existente.
        """
        instance.identificador_usuario = validated_data.get('identificador_usuario', instance.identificador_usuario)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.nombre_usuario = validated_data.get('nombre_usuario', instance.nombre_usuario)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.rut = validated_data.get('rut', instance.rut)
        instance.contraseña = validated_data.get('contraseña', instance.contraseña)
        instance.profesion = validated_data.get('profesion', instance.profesion)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.activo = validated_data.get('activo', instance.activo)
        instance.id_tipo_usuario = validated_data.get('id_tipo_usuario', instance.id_tipo_usuario)
        instance.save()
        return instance
