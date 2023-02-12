from core.enums.validation_enum import RegExEnum

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=128,
        validators=[
            V.MinLengthValidator(8),
            V.MaxLengthValidator(128),
            V.RegexValidator(RegExEnum.ContainOneNumber.pattern, RegExEnum.ContainOneNumber.msg),
            V.RegexValidator(RegExEnum.ContainNonAlphaNumeric.pattern, RegExEnum.ContainNonAlphaNumeric.msg),
            V.RegexValidator(RegExEnum.WhiteSpace.pattern, RegExEnum.WhiteSpace.msg, inverse_match=True),
            V.RegexValidator(RegExEnum.ContainUpperCaseLetter.pattern, RegExEnum.ContainUpperCaseLetter.msg),
            V.RegexValidator(RegExEnum.ContainerLowerCaseLetter.pattern, RegExEnum.ContainerLowerCaseLetter.msg)
        ]
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[
        V.RegexValidator(RegExEnum.OnlyWord.pattern, RegExEnum.OnlyWord.msg, code='iu')
    ])
    surname = models.CharField(max_length=20, validators=[
        V.RegexValidator(RegExEnum.OnlyWord.pattern, RegExEnum.OnlyWord.msg, code='iu')
    ])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
