# Generated by Django 4.2.3 on 2023-08-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comprar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('cvc', models.CharField(max_length=100)),
                ('exp_mes', models.CharField(max_length=3)),
                ('exp_year', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]