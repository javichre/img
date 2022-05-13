# Generated by Django 2.1.11 on 2022-03-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('Id_Ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['ciudad'],
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('Id_Nacionalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sexo',
            fields=[
                ('Id_Sexo', models.AutoField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(max_length=20)),
            ],
        ),
    ]
