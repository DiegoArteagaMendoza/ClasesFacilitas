from django.db import models
from django.db.models.deletion import RESTRICT, CASCADE
from .querysets import ListarUsuarios


class TiposUsuarios(models.Model):
    """
    Modelo para representar los tipos de usuarios.
    """
    id_tipo_usuario = models.AutoField("ID del tipo de usuario", primary_key=True)
    nombre_tipo = models.CharField("Nombre del tipo de usuario", max_length=50, unique=True)

    class Meta:
        db_table = 'tipos_usuarios'
        managed = False  # Indica que Django no gestionará esta tabla directamente

    def __str__(self):
        return f'Tipo de Usuario: {self.nombre_tipo}'


class Usuarios(models.Model):
    """
    Modelo para representar los usuarios.
    """
    id = models.AutoField("ID del usuario", primary_key=True)
    identificador_usuario = models.CharField("Identificador único del usuario", max_length=50, unique=True)
    nombre = models.CharField("Nombre del usuario", max_length=100)
    apellido = models.CharField("Apellido del usuario", max_length=100)
    nombre_usuario = models.CharField("Nombre de usuario", max_length=50, unique=True)
    correo = models.EmailField("Correo electrónico", max_length=100, unique=True)
    rut = models.CharField("RUT", max_length=20, unique=True)
    # Asegúrate de almacenar contraseñas de forma segura
    contraseña = models.CharField("Contraseña", max_length=255)
    profesion = models.CharField("Profesión", max_length=100, blank=True, null=True)
    descripcion = models.TextField("Descripción", blank=True, null=True)
    activo = models.BooleanField("Usuario activo", default=True)
    id_tipo_usuario = models.ForeignKey(
        TiposUsuarios,
        on_delete=RESTRICT,
        related_name="usuarios_tipos",
        db_column="id_tipo_usuario"
    )

    objects = ListarUsuarios.as_manager()

    class Meta:
        db_table = 'usuarios'
        managed = False  # Indica que Django no gestionará esta tabla directamente

    def __str__(self):
        return f'Usuario: {self.nombre_usuario} ({self.nombre} {self.apellido})'

    def crear(self, data):
        """
        Método para crear un nuevo usuario.
        """
        return Usuarios.objects.create(
            identificador_usuario=data.get('identificador_usuario'),
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            nombre_usuario=data.get('nombre_usuario'),
            correo=data.get('correo'),
            rut=data.get('rut'),
            contraseña=data.get('contraseña'),
            profesion=data.get('profesion'),
            descripcion=data.get('descripcion'),
            activo=data.get('activo', True),
            id_tipo_usuario_id=data.get('id_tipo_usuario')
        )
