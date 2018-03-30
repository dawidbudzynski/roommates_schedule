from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import (AddApartmentForm, AddRoommateForm, AddRoomForm, LoginForm)
from .models import (Apartment, Roommate, Room)


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

            return HttpResponseRedirect('/show_apartment')
        return HttpResponse('wrong_value')


class Showapartmensview(View):
    def get(self, request):
        all_apartments = Apartment.objects.all()
        ctx = {'all_apartments': all_apartments}

        return render(request,
                      template_name='apartments.html',
                      context=ctx)


class DeleteApartmentView(View):

    def get(self, request, apartment_id):
        apartment = Apartment.objects.get(id=apartment_id)
        apartment.user.delete()
        apartment.delete()

        return HttpResponseRedirect('/show_apartment')


# ROOMMATES

class AddRoommateView(LoginRequiredMixin, View):

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


class ShowRoommatesView(View):
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


# ROOMS

class AddRoomView(View):

    def get(self, request):
        form = AddRoomForm().as_p()
        ctx = {'form': form}

        return render(request,
                      template_name='add_room.html',
                      context=ctx)

    def post(self, request):
        form = AddRoomForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            apartment = form.cleaned_data['apartment']

            Room.objects.create(name=name, apartment=apartment)

            return HttpResponseRedirect('/show_room')
        return HttpResponse('wrong_value')


class ShowRoomsView(View):
    def get(self, request):
        all_rooms = Room.objects.all()
        ctx = {'all_rooms': all_rooms}

        return render(request,
                      template_name='rooms.html',
                      context=ctx)


class DeleteRoommView(View):

    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()

        return HttpResponseRedirect('/show_room')


# LOGIN

class LoginToApartmentView(View):
    def get(self, request):

        form = LoginForm().as_p()
        ctx = {
            'form': form
        }
        return render(request,
                      template_name='login.html',
                      context=ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/wrong_password')
        else:
            return HttpResponseRedirect('/wrong_value')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
