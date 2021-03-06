# Generated by Django 2.1.11 on 2022-04-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suscripciones', '0003_auto_20220404_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_medica',
            fields=[
                ('ordenmedicaid', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('hora', models.DateTimeField(blank=True, null=True)),
                ('admisionid', models.IntegerField(blank=True, null=True)),
                ('emergenciaid', models.IntegerField(blank=True, null=True)),
                ('pacienteid', models.IntegerField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('dieta', models.TextField(blank=True, null=True)),
                ('medicoid', models.IntegerField(blank=True, null=True)),
                ('usuarioid', models.IntegerField(blank=True, null=True)),
                ('estatus', models.CharField(blank=True, max_length=3, null=True)),
                ('uci', models.IntegerField()),
            ],
            options={
                'db_table': 'ordenmedica',
                'managed': False,
            },
        ),
    ]
