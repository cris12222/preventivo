# Generated by Django 3.0.5 on 2023-11-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='getFecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MetaModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('descripcion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'metas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'temas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('conferencia', models.IntegerField()),
                ('cursos', models.IntegerField()),
                ('escuela', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('apoyo', models.CharField(max_length=255)),
                ('cant_hombres', models.IntegerField()),
                ('cant_mujeres', models.IntegerField()),
                ('dirigido', models.CharField(max_length=255)),
                ('tema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='preventivocrud.Tema')),
            ],
            options={
                'db_table': 'eventos',
                'ordering': ['-id'],
            },
        ),
    ]