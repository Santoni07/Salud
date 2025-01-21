# Generated by Django 5.1.1 on 2025-01-18 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistroMedico', '0006_registromedico_fecha_de_llenado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtrosExamenesClinicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respiratorio_observaciones', models.TextField(default='Sin observaciones')),
                ('renal_observaciones', models.TextField(default='Sin observaciones')),
                ('digestivo_observaciones', models.TextField(default='Sin observaciones')),
                ('osteoarticular_observaciones', models.TextField(default='Sin observaciones')),
                ('ficha_medica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otros_examenes', to='RegistroMedico.registromedico')),
            ],
        ),
    ]
