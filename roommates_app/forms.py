from django.forms import (Form, CharField, PasswordInput, ChoiceField)

from .models import (Roommate, Room)

all_roommates = Roommate.objects.all()
all_rooms = Room.objects.all()
COLOURS = {('#E1361F', 'red'), ('#EAE530', 'yellow'), ('#F08322', 'orange'),
           ('#977F6A', 'gray'), ('#35A035', 'green'), ('#4A62C4', 'blue'), ('#4E2E7E', 'purple'),
           ('#47B7A6', 'light-blue')}


class AddAccountForm(Form):
    name = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password again', widget=PasswordInput)


class AddRoommateForm(Form):
    name = CharField(label='Name', strip=True)
    colour = ChoiceField(choices=COLOURS)


class AddRoomForm(Form):
    name = CharField(label='Name', strip=True)


class LoginForm(Form):
    username = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
