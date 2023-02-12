# Generated by Django 4.1.5 on 2023-02-12 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_usermodel_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zа-яёіA-ZА-ЯЇЁ]+$', 'enter only alphanumeric characters', code='iu')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zа-яёіA-ZА-ЯЇЁ]+$', 'enter only alphanumeric characters', code='iu')]),
        ),
    ]
