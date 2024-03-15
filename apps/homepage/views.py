# Libraries and modules
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from . import afunctions
from . import models
from . import forms

# Vistas para la aplicacion homepage


def inicio(request):
    return render(request, 'inicio.html')


def registrarse(request):
    if request.method == 'POST':
        form = forms.registrarse(request.POST)

        if form.is_valid():
            # Informacion de la cuenta
            nombre_usuario = form.cleaned_data['nombre_usuario']
            contrasena = form.cleaned_data['contrasena']
            confirmar_contrasena = form.cleaned_data['confirmar_contrasena']

            # Informacion personal
            nombre_completo = form.cleaned_data['nombre_completo']
            genero = form.cleaned_data['genero']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            correo_electronico = form.cleaned_data['correo_electronico']
            numero_telefono = form.cleaned_data['numero_telefono']
            estado = form.cleaned_data['estado']
            ciudad = form.cleaned_data['ciudad']

            # Informacion academica
            escuela = form.cleaned_data['escuela']
            tipo_escuela = form.cleaned_data['tipo_escuela']
            grado_academico = form.cleaned_data['grado_academico']

            if contrasena == confirmar_contrasena:
                if not User.objects.filter(username=nombre_usuario).exists():
                    try:
                        # Determinamos los examenes que el usuario puede tomar
                        examenes = afunctions.determinar_examenes(
                            grado_academico)

                        # Creamos el usuario para el modelo User de Django
                        user = User.objects.create_user(
                            username=nombre_usuario,
                            password=contrasena
                        )

                        user.save()

                        # Creamos el usuario para el modelo Estudiantes
                        estudiante = models.Estudiantes.objects.create(
                            # Modelo User de Django
                            user=user,

                            # Informacion de la cuenta
                            correo_electronico=correo_electronico,

                            # Informacion personal
                            nombre_completo=nombre_completo,
                            genero=genero,
                            fecha_nacimiento=fecha_nacimiento,
                            numero_telefono=numero_telefono,
                            estado=estado,
                            ciudad=ciudad,

                            # Informacion academica
                            escuela=escuela,
                            tipo_escuela=tipo_escuela,
                            grado_academico=grado_academico,
                        )

                        estudiante.save()

                        # Creamos el registro del estudiante en la tabla de examenes
                        examenes_estudiante = models.Examenes.objects.create(
                            # Modelo Estudiantes
                            id_estudiante=estudiante,

                            # Examenes
                            escolar=examenes[0],
                            benjamin=examenes[1],
                            cadete=examenes[2],
                            junior=examenes[3],
                            estudiante=examenes[4],
                        )

                        examenes_estudiante.save()

                        '''
                        # Creamos el template para el correo de confirmacion
                        template = render_to_string('correo_confirmacion.html', {
                            'nombre_completo': nombre_completo,
                        })

                        # Creamos el correo de confirmacion
                        email = EmailMessage(
                            'Correo de confirmación al Canguro Matemático Mexicano 2024',
                            template,
                            settings.EMAIL_HOST_USER,
                            [correo_electronico]
                        )

                        # Enviamos el correo de confirmacion
                        email.fail_silently = False
                        email.content_subtype = 'html'
                        email.send()

                        messages.success(
                            request, '¡Tu cuenta ha sido creada exitosamente!')

                        return redirect('inicio')
                        '''

                    except Exception as e:
                        # Eliminamos el usuario creado
                        user.delete()

                        messages.error(
                            request, 'Ha ocurrido un error al crear tu cuenta. Por favor, intenta de nuevo.')

                else:
                    messages.error(
                        request, 'El nombre de usuario ingresado ya está en uso.')

            else:
                messages.error(
                    request, 'Las contraseñas ingresadas no coinciden.')

        else:
            messages.error(
                request, 'Por favor, verifica la información ingresada.')

    else:
        form = forms.registrarse()

    return render(request, 'registrarse.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = forms.iniciar_sesion(request.POST)

        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            contrasena = form.cleaned_data['contrasena']

            if User.objects.filter(username=nombre_usuario).exists():

                user = authenticate(username=nombre_usuario,
                                    password=contrasena)

                if user is not None:
                    login(request, user)

                    messages.success(
                        request, f'Hola, {nombre_usuario}. ¡Has iniciado sesión exitosamente!')

                    return redirect('inicio')

                else:
                    messages.error(
                        request, 'El nombre de usuario o la contraseña ingresados son incorrectos.')

            else:
                messages.error(
                    request, 'El usuario con el que se está intentando ingresar, todavía no se encuentra registrado en el sistema.')

        else:
            messages.error(
                request, 'Por favor, verifica la información ingresada.')

    else:
        form = forms.iniciar_sesion()

    return render(request, 'iniciar_sesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)

    messages.success(
        request, '¡Tu sesión ha sido cerrada exitosamente!')

    return redirect('inicio')


def contacto(request):
    if request.method == 'POST':
        form = forms.contacto(request.POST)

        if form.is_valid():
            nombre_completo = form.cleaned_data['nombre_completo']
            correo_electronico = form.cleaned_data['correo_electronico']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            if asunto and mensaje and correo_electronico:
                try:
                    # Creamos el template para el correo
                    template = render_to_string('correo_contacto.html', {
                        'nombre_completo': nombre_completo,
                        'correo_electronico': correo_electronico,
                        'asunto': asunto,
                        'mensaje': mensaje,
                    })

                    # Creamos el correo
                    email = EmailMessage(
                        '[SOPORTE] ' + asunto,
                        template,
                        settings.EMAIL_HOST_USER,
                        ['ommcanguro@gmail.com']
                    )

                    # Enviamos el correo
                    email.fail_silently = False
                    email.send()

                    messages.success(
                        request, 'Tu mensaje ha sido enviado exitosamente. ¡Gracias por ponerte en contacto con nosotros!')

                    return redirect('contacto')

                except BadHeaderError:
                    messages.error(
                        request, 'Ha ocurrido un error al enviar tu mensaje. Por favor, intenta de nuevo.')

        else:
            messages.error(
                request, 'Por favor, verifica la información ingresada.')

    else:
        form = forms.contacto()

    return render(request, 'contacto.html', {'form': form})
