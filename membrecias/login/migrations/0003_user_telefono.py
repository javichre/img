# Generated by Django 2.1.11 on 2022-04-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20220325_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
