# Libraries and modules
from django.core.validators import RegexValidator
from django import forms
from . import afunctions

# Forms for the homepage app


class registrarse(forms.Form):
    # Informacion modelo User de Django
    nombre_usuario = forms.CharField(
        min_length=5,
        max_length=30,
        required=True,
        label='Nombre de usuario:',
        validators=[RegexValidator(
            regex=r"^[a-zA-Z0-9]+$", message='El nombre de usuario solo puede contener letras y números.')],
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'Ej. maria123', 'autofocus': True, 'autocomplete': 'off', 'title': 'Nombre de usuario.'}),
        error_messages={'required': 'El nombre de usuario es requerido.'}
    )

    contrasena = forms.CharField(
        min_length=8,
        max_length=16,
        required=True,
        label='Contraseña:',
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'placeholder': '********', 'autocomplete': 'off', 'title': 'Contraseña.'}),
    )

    confirmar_contrasena = forms.CharField(
        min_length=8,
        max_length=16,
        required=True,
        label='Confirmar contraseña:',
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'placeholder': '********', 'autocomplete': 'off', 'title': 'Confirmar contraseña.'}),
    )

    # Informacion de la cuenta
    correo_electronico = forms.EmailField(
        min_length=1,
        max_length=100,
        required=True,
        label='Correo electrónico:',
        widget=forms.EmailInput(
            attrs={'type': 'email', 'placeholder': 'Ej. maria@gmail.com', 'autocomplete': 'off', 'title': 'Correo electrónico.'}),
        error_messages={
            'invalid': 'El correo electrónico ingresado no es válido.'}
    )

    # Informacion personal
    nombre_completo = forms.CharField(
        min_length=1,
        max_length=100,
        required=True,
        label='Nombre completo:',
        widget=forms.TextInput(attrs={
                               'type': 'text', 'placeholder': 'Ej. María Pérez López', 'autocomplete': 'off', 'title': 'Nombre completo.'})
    )

    genero = forms.ChoiceField(
        required=True,
        label='Genero:',
        choices=(('F', 'Femenino'),
                 ('M', 'Masculino'),
                 ('O', 'Otro'),
                 )
    )

    fecha_nacimiento = forms.DateField(
        required=True,
        label='Fecha de nacimiento:',
        validators=[afunctions.validar_fecha_futura],
        widget=forms.DateInput(
            attrs={'type': 'date', 'autocomplete': 'off'}),
        error_messages={'invalid': 'La fecha ingresada no es válida.'}
    )

    numero_telefono = forms.CharField(
        min_length=10,
        max_length=10,
        required=True,
        label='Número de teléfono (10 dígitos):',
        validators=[RegexValidator(
            regex=r"^\d{10}$", message='El número de teléfono debe contener 10 dígitos.')],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ej. 0123456789', 'autocomplete': 'off', 'title': 'Número de teléfono.'})
    )

    estado = forms.ChoiceField(
        required=True,
        label='Estado:',
        choices=(('Aguascalientes', 'Aguascalientes'),
                 ('Baja California', 'Baja California'),
                 ('Baja California Sur', 'Baja California Sur'),
                 ('Campeche', 'Campeche'),
                 ('Chiapas', 'Chiapas'),
                 ('Chihuahua', 'Chihuahua'),
                 ('Ciudad de México', 'Ciudad de México'),
                 ('Coahuila', 'Coahuila'),
                 ('Colima', 'Colima'),
                 ('Durango', 'Durango'),
                 ('Estado de México', 'Estado de México'),
                 ('Guanajuato', 'Guanajuato'),
                 ('Guerrero', 'Guerrero'),
                 ('Hidalgo', 'Hidalgo'),
                 ('Jalisco', 'Jalisco'),
                 ('Michoacán', 'Michoacán'),
                 ('Morelos', 'Morelos'),
                 ('Nayarit', 'Nayarit'),
                 ('Nuevo León', 'Nuevo León'),
                 ('Oaxaca', 'Oaxaca'),
                 ('Puebla', 'Puebla'),
                 ('Querétaro', 'Querétaro'),
                 ('Quintana Roo', 'Quintana Roo'),
                 ('San Luis Potosí', 'San Luis Potosí'),
                 ('Sinaloa', 'Sinaloa'),
                 ('Sonora', 'Sonora'),
                 ('Tabasco', 'Tabasco'),
                 ('Tamaulipas', 'Tamaulipas'),
                 ('Tlaxcala', 'Tlaxcala'),
                 ('Veracruz', 'Veracruz'),
                 ('Yucatán', 'Yucatán'),
                 ('Zacatecas', 'Zacatecas'),
                 )
    )

    ciudad = forms.CharField(
        min_length=1,
        max_length=100,
        required=True,
        label='Ciudad/población/localidad:',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ej. Morelia', 'autocomplete': 'off', 'title': 'Ciudad/población/localidad.'})
    )

    # Informacion academica
    escuela = forms.CharField(
        min_length=1,
        max_length=120,
        required=True,
        label='Escuela:',
        widget=forms.TextInput(attrs={
                               'class': 'form-control', 'placeholder': 'Ej. Escuela Primaria Hijos del Ejército', 'autocomplete': 'off',
                               'title': 'Escuela.'})
    )

    tipo_escuela = forms.ChoiceField(
        required=True,
        label='Tipo de escuela:',
        choices=(('Pública', 'Pública'),
                 ('Privada', 'Privada'),
                 )
    )

    grado_academico = forms.ChoiceField(
        required=True,
        label='Grado escolar:',
        choices=(
            ('1° de primaria', '1° de primaria'),
            ('2° de primaria', '2° de primaria'),
            ('3° de primaria', '3° de primaria'),
            ('4° de primaria', '4° de primaria'),
            ('5° de primaria', '5° de primaria'),
            ('6° de primaria', '6° de primaria'),
            ('1° de secundaria', '1° de secundaria'),
            ('2° de secundaria', '2° de secundaria'),
            ('3° de secundaria', '3° de secundaria'),
            ('1° de preparatoria', '1° de preparatoria'),
            ('2° de preparatoria', '2° de preparatoria'),
            ('3° de preparatoria', '3° de preparatoria'),
        )
    )


class iniciar_sesion(forms.Form):
    nombre_usuario = forms.CharField(
        min_length=5,
        max_length=30,
        required=True,
        label='Nombre de usuario:',
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'Ej. maria123', 'autofocus': True, 'autocomplete': 'off', 'title': 'Nombre de usuario.'}),
        error_messages={'required': 'El nombre de usuario es requerido.'}
    )

    contrasena = forms.CharField(
        min_length=8,
        max_length=16,
        required=True,
        label='Contraseña:',
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'placeholder': '********', 'autocomplete': 'off', 'title': 'Contraseña.'}),
    )


class contacto(forms.Form):
    nombre_completo = forms.CharField(
        min_length=1,
        max_length=100,
        required=True,
        label='Nombre completo:',
        widget=forms.TextInput(attrs={
                               'class': 'form-control', 'placeholder': 'Ej. María Pérez López', 'autocomplete': 'off', 'title': 'Nombre completo.'})
    )

    correo_electronico = forms.EmailField(
        min_length=1,
        max_length=100,
        required=True,
        label='Correo electrónico:',
        widget=forms.EmailInput(
            attrs={'type': 'email', 'placeholder': 'Ej. maria@gmail.com', 'autocomplete': 'off', 'title': 'Correo electrónico.'}),
        error_messages={
            'invalid': 'El correo electrónico ingresado no es válido.'}
    )

    asunto = forms.CharField(
        min_length=1,
        max_length=100,
        required=True,
        label='Asunto:',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ej. Problemas al registrarme', 'autocomplete': 'off', 'title': 'Asunto.'})
    )

    mensaje = forms.CharField(
        min_length=1,
        required=True,
        label='Mensaje:',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Escribe aquí tu mensaje...', 'autocomplete': 'off', 'title': 'Mensaje.'})
    )