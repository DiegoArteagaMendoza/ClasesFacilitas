from django.db import models
from django.db.models import Q, F, Case, When, Value
from django.db.models.functions import Concat


class ListarUsuarios(models.QuerySet):
    def consultar_listado_administradores(self):
        """
        Consulta para obtener los usuarios administradores.
        """
        # Filtrar usuarios cuyo tipo de usuario sea "Administrador" (id_tipo_usuario=1)
        query = self.filter(id_tipo_usuario=1)

        # Optimizar la consulta seleccionando solo los campos necesarios
        query = query.values(
            'id',
            'nombre',
            'apellido',
            'nombre_usuario',
            'correo',
            'rut',
            'profesion',
            'descripcion',
            'activo'
        )

        # # Agregar un campo calculado (opcional)
        # query = query.annotate(
        #     nombre_completo=Concat(F('nombre'), Value(' '), F(
        #         'apellido'), output_field=models.CharField())
        # )

        # Devolver el QuerySet
        return query
