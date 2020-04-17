# Generated by Django 3.0.5 on 2020-04-17 09:08

import covid_update.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_update', '0004_paises'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualizacion',
            old_name='ultima_actualizacion',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='actualizacion',
            name='archivo',
            field=models.FilePathField(path=covid_update.models.obtener_directorio_casos, unique=True),
        ),
    ]