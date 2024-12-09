# Generated by Django 4.2.7 on 2023-12-14 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Dependienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField(auto_now=True)),
                ('servicio', models.CharField(max_length=100)),
                ('dependienta', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='programacion.dependienta')),
                ('nombre', models.ManyToManyField(to='programacion.cliente')),
            ],
        ),
    ]