# Generated by Django 5.1.1 on 2024-10-28 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0002_remove_medico_registro_medico'),
        ('RegistroMedico', '0003_cardiovascular_electrobasal_electroesfuerzo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromedico',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Medico.medico'),
        ),
    ]
