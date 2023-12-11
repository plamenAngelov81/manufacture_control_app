from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


class Employee(AbstractUser):
    USER_NAME_MAX_LEN = 35
    USER_NAME_MIN_LEN = 5
    PASSWORD_MAX_LEN = 25
    PASSWORD_MIN_LEN = 8
    AGE_MIN_VALUE = 18
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 3

    user_id = models.CharField(
        verbose_name='Username',
        max_length=USER_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(USER_NAME_MIN_LEN)],
        unique=True
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(FIRST_NAME_MIN_LEN)]
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(LAST_NAME_MIN_LEN)]
    )

    @property
    def get_name(self):
        first = ''
        last = ''
        if self.first_name:
            first = self.first_name
        if self.last_name:
            last = self.last_name
        return f"{first} {last}"
