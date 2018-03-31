from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
import calendar

from .forms import (AddAccountForm, AddRoommateForm, AddRoomForm, LoginForm, AddCleaningForm)
from .models import (Roommate, Room, Cleaning)


# APARTMENTS

class AddAccountView(View):

    def get(self, request):

        form = AddAccountForm().as_p()
        ctx = {'form': form}

        return render(request,
                      template_name='add_account.html',
                      context=ctx)

    def post(self, request):
        form = AddAccountForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                return HttpResponse("wrong_password")
            if User.objects.filter(username=username).exists():
                return HttpResponse('object_already_exist')

            User.objects.create_user(username=username, password=password)

            return HttpResponseRedirect('/show_account')
        return HttpResponse('wrong_value')


class ShowAccountView(View):
    def get(self, request):
        all_users = User.objects.all()
        ctx = {'all_users': all_users}

        return render(request,
                      template_name='users.html',
                      context=ctx)


class DeleteAccountView(View):

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()

        return HttpResponseRedirect('/show_account')


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
            colour = form.cleaned_data['colour']
            if request.user.is_authenticated:
                account = request.user
                Roommate.objects.create(name=name, account=account, colour=colour)

            return HttpResponseRedirect('/show_roommate')
        return HttpResponse('wrong_value')


class ShowRoommatesView(LoginRequiredMixin, View):
    def get(self, request):
        all_roommates = Roommate.objects.all()
        ctx = {'all_roommates': all_roommates}

        return render(request,
                      template_name='roommates.html',
                      context=ctx)


class DeleteRoommateView(LoginRequiredMixin, View):

    def get(self, request, roommate_id):
        roommate = Roommate.objects.get(id=roommate_id)
        roommate.delete()

        return HttpResponseRedirect('/show_roommate')


# ROOMS

class AddRoomView(LoginRequiredMixin, View):

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
            if request.user.is_authenticated:
                account = request.user
                Room.objects.create(name=name, account=account)

            return HttpResponseRedirect('/show_room')
        return HttpResponse('wrong_value')


class ShowRoomsView(LoginRequiredMixin, View):
    def get(self, request):
        all_rooms = Room.objects.all()
        ctx = {'all_rooms': all_rooms}

        return render(request,
                      template_name='rooms.html',
                      context=ctx)


class DeleteRoomView(LoginRequiredMixin, View):

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


# CLEANING

class AddCleaningView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddCleaningForm()
        all_rooms = Room.objects.all()
        all_roommates = Roommate.objects.all()

        ctx = {'form': form,
               'all_roommates':all_roommates,
               'all_rooms':all_rooms}

        return render(request,
                      template_name='add_cleaning.html',
                      context=ctx)

    def post(self, request):

        # week_1

        roommate_result_id = request.POST['roommate_week_1']
        room_result_id = request.POST['room_week_1']
        selected_roommate_1 = Roommate.objects.get(id=roommate_result_id)
        selected_room_1 = Room.objects.get(id=room_result_id)
        Cleaning.objects.create(roommate=selected_roommate_1, room=selected_room_1)

        # week_2

        roommate_result_id = request.POST['roommate_week_2']
        room_result_id = request.POST['room_week_2']
        selected_roommate_2 = Roommate.objects.get(id=roommate_result_id)
        selected_room_2 = Room.objects.get(id=room_result_id)
        Cleaning.objects.create(roommate=selected_roommate_2, room=selected_room_2)

        # week_3

        roommate_result_id = request.POST['roommate_week_3']
        room_result_id = request.POST['room_week_3']
        selected_roommate_3 = Roommate.objects.get(id=roommate_result_id)
        selected_room_3 = Room.objects.get(id=room_result_id)
        Cleaning.objects.create(roommate=selected_roommate_3, room=selected_room_3)

        # week_4

        roommate_result_id = request.POST['roommate_week_4']
        room_result_id = request.POST['room_week_4']
        selected_roommate_4 = Roommate.objects.get(id=roommate_result_id)
        selected_room_4 = Room.objects.get(id=room_result_id)
        Cleaning.objects.create(roommate=selected_roommate_4, room=selected_room_4)

        # week_5

        roommate_result_id = request.POST['roommate_week_5']
        room_result_id = request.POST['room_week_5']
        selected_roommate_5 = Roommate.objects.get(id=roommate_result_id)
        selected_room_5 = Room.objects.get(id=room_result_id)
        Cleaning.objects.create(roommate=selected_roommate_5, room=selected_room_5)


        ctx = {'week_1_colour': selected_roommate_1.colour,
               'week_2_colour': selected_roommate_2.colour,
               'week_3_colour': selected_roommate_3.colour,
               'week_4_colour': selected_roommate_4.colour,
               'week_5_colour': selected_roommate_5.colour}

        return render(request,
                      template_name='add_cleaning.html',
                      context=ctx)


class ShowCleaningView(LoginRequiredMixin, View):
    def get(self, request):
        all_cleaning = Cleaning.objects.all()
        c = calendar.HTMLCalendar(calendar.MONDAY)
        cal = c.formatmonth(2018, 4)

        ctx = {'all_cleaning': all_cleaning,
               'cal': cal}

        return render(request,
                      template_name='cleaning.html',
                      context=ctx)


class DeleteCleaningView(LoginRequiredMixin, View):

    def get(self, request, cleaning_id):
        cleaning = Cleaning.objects.get(id=cleaning_id)
        cleaning.delete()

        return HttpResponseRedirect('/show_cleaning')
