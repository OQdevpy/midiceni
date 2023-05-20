from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from apps.accounts.models import User


class AccountCreationForm(UserCreationForm):
    phone_number = PhoneNumberField(region="UZ")

    class Meta:
        model = User
        fields = ["username", "phone_number", "user_roles", "password1", "password2"]
        labels = {
            "username": "Name",
        }

    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
