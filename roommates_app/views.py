from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import (AddApartmentForm, AddRoommateForm)
from .models import (Apartment, Roommate)


# APARTMENTS

class AddApartmentView(View):

    def get(self, request):

        form = AddApartmentForm().as_p()
        ctx = {'form': form}

        return render(request,
                      template_name='add_apartment.html',
                      context=ctx)

    def post(self, request):
        form = AddApartmentForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                return HttpResponse("wrong_password")
            if User.objects.filter(username=name).exists():
                return HttpResponse('object_already_exist')

            new_user = User.objects.create_user(username=name, password=password)
            Apartment.objects.create(user=new_user)

            return HttpResponse('apartment created')
        return HttpResponse('wrong_value')

class ShowApartmensView(View):
    def get(self, request):
        all_apartments = Apartment.objects.all()
        ctx = {'all_apartments': all_apartments}

        return render(request,
                      template_name='apartments.html',
                      context=ctx)

# ROOMMATES

class AddRoommatetView(View):

    def get(self, request):

        form = AddRoommateForm().as_p()
        ctx = {'form': form}

        return render(request,
                      template_name='add_roommate.html',
                      context=ctx)

    def post(self, request):
        form = AddRoommateForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            apartment = form.cleaned_data['apartment']
            Roommate.objects.create(name=name, apartment=apartment)

            return HttpResponseRedirect('/show_roommate')
        return HttpResponse('wrong_value')

class ShowRoommatedView(View):
    def get(self, request):
        all_roommates = Roommate.objects.all()
        ctx = {'all_roommates': all_roommates}

        return render(request,
                      template_name='roommates.html',
                      context=ctx)

class DeleteRoommateView(View):

    def get(self, request, roommate_id):
        roommate = Roommate.objects.get(id=roommate_id)
        roommate.delete()

        return HttpResponseRedirect('/show_roommate')

