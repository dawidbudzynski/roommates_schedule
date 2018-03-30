from django.forms import (Form, CharField, ModelChoiceField, PasswordInput, DateField,SelectDateWidget)

from .models import (Roommate, Room)

all_roommates = Roommate.objects.all()
all_rooms = Room.objects.all()


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


class AddCleaningForm(Form):
    roommate = ModelChoiceField(label='Who cleaned?', queryset=all_roommates)
    room = ModelChoiceField(label='Which room?', queryset=all_rooms)
    date = DateField(label='When?', widget=SelectDateWidget)
