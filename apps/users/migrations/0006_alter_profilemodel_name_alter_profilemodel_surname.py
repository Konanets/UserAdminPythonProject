# Generated by Django 4.1.5 on 2023-02-10 21:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profilemodel_name_alter_profilemodel_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯїЇёЁ]+$', 'enter only alphanumeric characters')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-ЯїЇёЁ]+$', 'enter only alphanumeric characters')]),
        ),
    ]
