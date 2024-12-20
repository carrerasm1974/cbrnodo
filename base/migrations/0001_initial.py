# Generated by Django 5.1.1 on 2024-12-18 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanalAnalogicoCarga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20)),
                ('escala', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=20)),
                ('valor_actual', models.FloatField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CanalAnalogicoEH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20)),
                ('escala', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=20)),
                ('valor_actual', models.FloatField()),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperacionesCbr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsample', models.FloatField()),
                ('ts', models.DateTimeField()),
                ('reason', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmaCargaSetpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Alta', 'Alta'), ('Baja', 'Baja')], max_length=50)),
                ('valor', models.FloatField()),
                ('habilitada', models.BooleanField(default=True)),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarmas', to='base.canalanalogicocarga')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='MuestrasICbr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v0', models.FloatField(null=True)),
                ('v1', models.FloatField(null=True)),
                ('v2', models.FloatField(null=True)),
                ('v3', models.FloatField(null=True)),
                ('v4', models.FloatField(null=True)),
                ('v5', models.FloatField(null=True)),
                ('v6', models.FloatField(null=True)),
                ('v7', models.FloatField(null=True)),
                ('op_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operacion', to='base.operacionescbr')),
            ],
        ),
    ]
