# Generated by Django 5.1.1 on 2024-10-15 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroMedico',
            fields=[
                ('idfichaMedica', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, choices=[('PENDIENTE', 'Pendiente'), ('PROCESO', 'En proceso'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], max_length=45, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_caducidad', models.DateField()),
                ('observacion', models.CharField(blank=True, max_length=200, null=True)),
                ('consentimiento_persona', models.BooleanField(blank=True, null=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.jugador')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.torneo')),
            ],
            options={
                'db_table': 'fichaRegistro',
            },
        ),
        migrations.CreateModel(
            name='AntecedenteEnfermedades',
            fields=[
                ('idantecedente_enfermedades', models.AutoField(primary_key=True, serialize=False)),
                ('fue_operado', models.BooleanField(blank=True, default=None, null=True)),
                ('toma_medicacion', models.BooleanField(blank=True, default=None, null=True)),
                ('estuvo_internado', models.BooleanField(blank=True, default=None, null=True)),
                ('sufre_hormigueos', models.BooleanField(blank=True, default=None, null=True)),
                ('es_diabetico', models.BooleanField(blank=True, default=None, null=True)),
                ('es_amatico', models.BooleanField(blank=True, default=None, null=True)),
                ('es_alergico', models.BooleanField(blank=True, default=None, null=True)),
                ('alerg_observ', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('antecedente_epilepsia', models.BooleanField(blank=True, default=None, null=True)),
                ('desviacion_columna', models.BooleanField(blank=True, default=None, null=True)),
                ('dolor_cintira', models.BooleanField(blank=True, default=None, null=True)),
                ('fracturas', models.BooleanField(blank=True, default=None, null=True)),
                ('dolores_articulares', models.BooleanField(blank=True, default=None, null=True)),
                ('falta_aire', models.BooleanField(blank=True, default=None, null=True)),
                ('tramatismos_craneo', models.BooleanField(blank=True, default=None, null=True)),
                ('dolor_pecho', models.BooleanField(blank=True, default=None, null=True)),
                ('perdida_conocimiento', models.BooleanField(blank=True, default=None, null=True)),
                ('presion_arterial', models.BooleanField(blank=True, default=None, null=True)),
                ('muerte_subita_familiar', models.BooleanField(blank=True, default=None, null=True)),
                ('enfermedad_cardiaca_familiar', models.BooleanField(blank=True, default=None, null=True)),
                ('soplo_cardiaco', models.BooleanField(blank=True, default=None, null=True)),
                ('abstenerce_competencia', models.BooleanField(blank=True, default=None, null=True)),
                ('antecedentes_coronarios_familiares', models.BooleanField(blank=True, default=None, null=True)),
                ('fumar_hipertension_diabetes', models.BooleanField(blank=True, default=None, null=True)),
                ('fhd_observacion', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('consumo_cocaina_anabolicos', models.BooleanField(blank=True, default=None, null=True)),
                ('cca_observaciones', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('idfichaMedica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RegistroMedico.registromedico')),
            ],
            options={
                'db_table': 'antecedente_enfermedades',
            },
        ),
    ]
