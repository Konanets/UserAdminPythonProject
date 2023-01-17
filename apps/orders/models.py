from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from apps.groups.models import GroupModel
from apps.users.models import UserModel as User

UserModel: type[User] = get_user_model()


class OrderModel(models.Model):
    class Meta:
        db_table = 'orders'

    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=35, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12, null=True)
    age = models.IntegerField(validators=[
        V.MinValueValidator(16),
        V.MaxValueValidator(90)
    ], null=True)
    course = models.CharField(null=True, max_length=100)
    course_format = models.CharField(null=True, max_length=100)
    course_type = models.CharField(null=True, max_length=100)
    sum = models.IntegerField(null=True)
    alreadyPaid = models.IntegerField(null=True)
    group = models.OneToOneField(GroupModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    utm = models.CharField(null=True, max_length=100)
    msg = models.CharField(null=True, max_length=100)
    status = models.BooleanField(null=True)
    manager = models.OneToOneField(UserModel, on_delete=models.SET_NULL, null=True)


class CommentModel(models.Model):
    class Meta:
        db_table = 'comments'

    comment = models.CharField(max_length=255, validators=[V.MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='comments')
