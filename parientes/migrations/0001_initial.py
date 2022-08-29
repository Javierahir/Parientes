# Generated by Django 4.1 on 2022-08-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Primo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=64)),
                ('fecha_de_entrega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sobrino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=64)),
                ('fecha_de_entrega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=64)),
                ('fecha_de_entrega', models.DateField()),
            ],
        ),
    ]