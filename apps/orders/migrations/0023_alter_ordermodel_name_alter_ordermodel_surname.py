# Generated by Django 4.1.5 on 2023-02-12 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_commentmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zа-яёіA-ZА-ЯЇЁ]+$', 'enter only alphanumeric characters', code='iu')]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='surname',
            field=models.CharField(max_length=35, null=True, validators=[django.core.validators.RegexValidator('^[a-zа-яёіA-ZА-ЯЇЁ]+$', 'enter only alphanumeric characters', code='iu')]),
        ),
    ]
