# Generated by Django 3.0.5 on 2020-04-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='id_registro',
            field=models.CharField(default='NA', help_text='Identificador en la liberada más reciente.', max_length=80),
            preserve_default=False,
        ),
    ]