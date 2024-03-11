# Generated by Django 5.0.2 on 2024-03-09 01:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_rename_schooltype_users_profiles_school_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_electronico', models.CharField(max_length=100)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_telefono', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=100)),
                ('escuela', models.CharField(max_length=120)),
                ('tipo_escuela', models.CharField(max_length=10)),
                ('grado_academico', models.CharField(max_length=30)),
                ('escolar', models.BooleanField()),
                ('benjamin', models.BooleanField()),
                ('cadete', models.BooleanField()),
                ('junior', models.BooleanField()),
                ('estudiante', models.BooleanField()),
                ('calificacion_escolar', models.FloatField(default=0.0, null=True)),
                ('calificacion_benjamin', models.FloatField(default=0.0, null=True)),
                ('calificacion_cadete', models.FloatField(default=0.0, null=True)),
                ('calificacion_junior', models.FloatField(default=0.0, null=True)),
                ('calificacion_estudiante', models.FloatField(default=0.0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='users_profiles',
        ),
    ]
