from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )

    nickname = models.CharField(verbose_name='닉네임', max_length=20, null=True)
    birth_date = models.DateField(verbose_name='생년월일', null=True)
    gender = models.CharField(
        verbose_name='성별', max_length=1, choices=GENDERS, null=True)
    introduce = models.TextField(verbose_name='자기소개', null=True)

    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
