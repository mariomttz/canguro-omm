# Libraries and modules
from django.core.validators import ValidationError
from datetime import date

# Funciones auxiliares


def validar_fecha_futura(fecha):
    if fecha > date.today():
        raise ValidationError(
            'La fecha de nacimiento no puede ser en el futuro.')


def determinar_examenes(grado):
    """
    Indice 0: Escolar
    Indice 1: Benjamín
    Indice 2: Cadete
    Indice 3: Junior
    Indice 4: Estudiante
    """
    if grado in ['1° de primaria', '2° de primaria', '3° de primaria', '4° de primaria', '5° de primaria']:
        return [True, True, True, True, True]

    elif grado in ['6° de primaria', '1° de secundaria']:
        return [False, True, True, True, True]

    elif grado == '2° de secundaria':
        return [False, False, True, True, True]

    elif grado in ['3° de secundaria', '1° de preparatoria', '2° de preparatoria']:
        return [False, False, False, True, True]

    elif grado == '3° de preparatoria':
        return [False, False, False, False, True]
