from django.db import models


class CourseFormatChoice(models.TextChoices):
    STATIC = 'static',
    ONLINE = 'online'


class CourseTypeChoice(models.TextChoices):
    PRO = 'pro'
    MINIMAL = 'minimal'
    PREMIUM = 'premium'
    INCUBATOR = 'incubator'
    VIP = 'vip'


class CoursesChoice(models.TextChoices):
    FS = 'FS'
    QACX = 'QACX'
    JCX = 'JCX'
    JSCX = 'JSCX'
    FE = 'FE'
    PCX = 'PCX'


class StatusChoice(models.TextChoices):
    IN_WORK = 'В работе'
    NEW = 'Новый'
    AGREE = 'Согласен'
    DISAGREE = 'Не согласен'
    DUBBLING = 'Дубляж'
