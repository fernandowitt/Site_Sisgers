# Generated by Django 2.1.12 on 2019-11-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vistoria',
            name='deferido',
            field=models.BooleanField(default=False),
        ),
    ]
