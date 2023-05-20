from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel

# Create your models here.
DOCTOR, PATIENT = (
    "doctor",
    "patient",
)


class User(AbstractUser, BaseModel):
    USER_ROLES = (
        (DOCTOR, DOCTOR),
        (PATIENT, PATIENT),
    )
    phone_number = PhoneNumberField(blank=True)
    user_roles = models.CharField(max_length=31, choices=USER_ROLES, default=PATIENT)

    objects = UserManager()

    def __str__(self):
        return str(self.username)
