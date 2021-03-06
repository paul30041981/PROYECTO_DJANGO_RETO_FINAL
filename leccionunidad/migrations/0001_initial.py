# Generated by Django 3.1.7 on 2021-03-28 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidadcurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leccionunidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc_corta', models.CharField(max_length=100)),
                ('desc_larga', models.CharField(max_length=255)),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidadcurso.unidadcurso')),
            ],
            options={
                'verbose_name_plural': 'Leccionunidades',
            },
        ),
    ]
