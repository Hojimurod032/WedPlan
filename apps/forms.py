import re
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'tg_username', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password = make_password(password)
        return password

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number = re.sub(r'\D', "", phone_number)

        user_data = User.objects.filter(phone_number=phone_number)
        if user_data:
            raise ValidationError("Phone number already exists")
        return phone_number


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'password')

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(**kwargs)

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_number = re.sub(r'\D', "", phone_number)
        password = self.cleaned_data.get('password')

        user_data = User.objects.filter(phone_number=phone_number).first()
        if not user_data:
            raise ValidationError("Phone number does not exist")
        if not check_password(password, user_data.password):
            raise ValidationError("Incorrect password")

        login(self.request, user_data)
