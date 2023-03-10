# Generated by Django 4.1.5 on 2023-01-18 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profilemodel'),
        ('orders', '0009_alter_ordermodel_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='users.profilemodel'),
        ),
    ]
