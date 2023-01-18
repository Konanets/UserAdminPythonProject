# Generated by Django 4.1.5 on 2023-01-17 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='course',
            field=models.CharField(choices=[('FS', 'FS'), ('QACX', 'QACX'), ('JCX', 'JCX'), ('JSCX', 'JSCX'), ('FE', 'FE'), ('PCX', 'PCX')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯїЇ]*$', 'enter only alphanumeric characters')]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator('^([+]?[\\s0-9]+)?(\\d{3}|[(]?[0-9]+[)])?([-]?[\\s]?[0-9])+$', 'invalid phone number')]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='surname',
            field=models.CharField(max_length=35, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯїЇ]*$', 'enter only alphanumeric characters')]),
        ),
    ]
