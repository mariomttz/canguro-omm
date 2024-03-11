# Libraries and modules
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Estudiantes(models.Model):
    # Modelo User de Django
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # Informacion de la cuenta
    correo_electronico = models.CharField(
        max_length=100,
        null=False
    )

    # Informacion personal
    nombre_completo = models.CharField(
        max_length=100,
        null=False
    )

    genero = models.CharField(
        max_length=1,
        null=False
    )

    fecha_nacimiento = models.DateField(
        null=False
    )

    numero_telefono = models.CharField(
        max_length=10,
        null=False,
    )

    estado = models.CharField(
        max_length=30,
        null=False
    )

    ciudad = models.CharField(
        max_length=100,
        null=False
    )

    # Informacion academica
    escuela = models.CharField(
        max_length=120,
        null=False
    )

    tipo_escuela = models.CharField(
        max_length=10,
        null=False
    )

    grado_academico = models.CharField(
        max_length=30,
        null=False
    )


class Examenes(models.Model):
    # Relacion con el modelo Estudiantes
    id_estudiante = models.OneToOneField(
        Estudiantes,
        on_delete=models.CASCADE
    )

    # Examenes
    escolar = models.BooleanField(
        null=False
    )

    benjamin = models.BooleanField(
        null=False
    )

    cadete = models.BooleanField(
        null=False
    )

    junior = models.BooleanField(
        null=False
    )

    estudiante = models.BooleanField(
        null=False
    )

    # Calificaciones de los examenes
    calificacion_escolar = models.FloatField(
        default=0.0,
        null=True
    )

    calificacion_benjamin = models.FloatField(
        default=0.0,
        null=True
    )

    calificacion_cadete = models.FloatField(
        default=0.0,
        null=True
    )

    calificacion_junior = models.FloatField(
        default=0.0,
        null=True
    )

    calificacion_estudiante = models.FloatField(
        default=0.0,
        null=True
    )
