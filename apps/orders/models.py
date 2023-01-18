from core.enums.choice_enum import ChoiceEnum
from core.enums.validation_enum import RegExEnum

from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from apps.groups.models import GroupModel
from apps.users.models import ProfileModel


class OrderModel(models.Model):
    class Meta:
        db_table = 'orders'
        ordering = ['-id']

    name = models.CharField(max_length=20, null=True,
                            validators=[V.RegexValidator(RegExEnum.OnlyWord.pattern, RegExEnum.OnlyWord.msg)])
    surname = models.CharField(max_length=35, null=True,
                               validators=[V.RegexValidator(RegExEnum.OnlyWord.pattern, RegExEnum.OnlyWord.msg)])
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12, null=True,
                             validators=[V.RegexValidator(RegExEnum.PhoneNumber.pattern, RegExEnum.PhoneNumber.msg)])
    age = models.IntegerField(validators=[
        V.MinValueValidator(16),
        V.MaxValueValidator(90)
    ], null=True)
    course = models.CharField(null=True, max_length=10, choices=ChoiceEnum.Courses)
    course_format = models.CharField(null=True, max_length=15, choices=ChoiceEnum.CourseFormat)
    course_type = models.CharField(null=True, max_length=100, choices=ChoiceEnum.CourseType)
    sum = models.IntegerField(null=True, validators=[
        V.MinValueValidator(1),
        V.MaxLengthValidator(2147483647)
    ])
    alreadyPaid = models.IntegerField(null=True, validators=[
        V.MinValueValidator(1),
        V.MaxLengthValidator(2147483647)
    ])
    group = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    utm = models.CharField(null=True, max_length=100, validators=[
        V.MinValueValidator(1),
    ])
    msg = models.CharField(null=True, max_length=100, validators=[
        V.MinValueValidator(1)
    ])
    status = models.BooleanField(null=True)
    manager = models.ForeignKey(ProfileModel, on_delete=models.SET_NULL, null=True, related_name='orders')


class CommentModel(models.Model):
    class Meta:
        db_table = 'comments'

    comment = models.CharField(max_length=255, validators=[V.MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='comments')
