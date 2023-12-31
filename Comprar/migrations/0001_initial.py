# Generated by Django 4.2.3 on 2023-07-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosNequi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreApellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=1000)),
                ('plan', models.CharField(max_length=50)),
                ('metodo', models.CharField(max_length=50)),
            ],
        ),
    ]
