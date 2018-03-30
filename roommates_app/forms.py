from django.contrib.auth.models import User
from django.forms import (Form, CharField, ModelChoiceField, PasswordInput)

all_accounts = User.objects.all()


class AddAccountForm(Form):
    name = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password again', widget=PasswordInput)


class AddRoommateForm(Form):
    name = CharField(label='Name', strip=True)

class AddRoomForm(Form):
    name = CharField(label='Name', strip=True)

class LoginForm(Form):
    username = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
