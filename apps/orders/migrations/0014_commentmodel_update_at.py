# Generated by Django 4.1.5 on 2023-02-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_ordermodel_alreadypaid_alter_ordermodel_msg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
