# Generated by Django 3.0.5 on 2020-09-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='dni',
            field=models.CharField(max_length=10, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name='Telefono'),
        ),
    ]