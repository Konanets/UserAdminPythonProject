from django.core import validators as V
from django.db import models


class GroupModel(models.Model):
    class Meta:
        db_table = 'groups'

    name = models.CharField(
        max_length=128,
        validators=[
            V.MinLengthValidator(4),
            V.MaxLengthValidator(128)
        ])
