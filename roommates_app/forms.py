from django.forms import (Form, CharField, ChoiceField, ModelChoiceField, Textarea, PasswordInput,
                          ImageField, ModelMultipleChoiceField, CheckboxSelectMultiple, Select,
                          EmailField, NullBooleanField)

from .models import Apartment

all_apartments = Apartment.objects.all()

class AddApartmentForm(Form):
    name = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password again', widget=PasswordInput)

class AddRoommateForm(Form):
    name = CharField(label='Name', strip=True)
    apartment = ModelChoiceField(queryset=all_apartments)
