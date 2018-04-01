from operator import itemgetter

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from .calendar_days import sorted_all_month_info
from .forms import (AddAccountForm, AddRoommateForm, AddRoomForm, LoginForm)
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
        all_rooms = Room.objects.all().order_by('name')
        all_roommates = Roommate.objects.all().order_by('name')

        all_months_info = []

        all_weeks_info = []
        for i in range(1, 64):
            single_week_info = {}
            single_week_info.update({'week': i})
            all_weeks_info.append(single_week_info)
        sorted_all_weeks_info = sorted(all_weeks_info, key=itemgetter('week'))

        for j in range(0, 12):
            single_month_info = {}
            single_month_info.update({'month': j, 'sorted_all_month_info': sorted_all_month_info[j]})
            all_months_info.append(single_month_info)

        ctx = {'all_roommates': all_roommates,
               'all_rooms': all_rooms,
               'all_months_info': all_months_info,
               'sorted_all_weeks_info': sorted_all_weeks_info}

        return render(request,
                      template_name='add_cleaning.html',
                      context=ctx)

    def post(self, request):

        all_weeks_info = []
        for i in range(1, 442):
            single_week_info = {}
            roommate_result_id = request.POST['roommate_index_{}'.format(i)]
            room_result_id = request.POST['room_index_{}'.format(i)]
            selected_roommate = Roommate.objects.get(id=roommate_result_id)
            selected_room = Room.objects.get(id=room_result_id)

            if Cleaning.objects.filter(week=i).exists():
                Cleaning.objects.filter(week=i).delete()
            Cleaning.objects.create(roommate=selected_roommate, room=selected_room, week=i)

            single_week_info.update({'day': i, 'selected_roommate': selected_roommate, 'selected_room': selected_room})
            all_weeks_info.append(single_week_info)

        sorted_all_weeks_info = sorted(all_weeks_info, key=itemgetter('day'))
        ctx = {
            'sorted_all_weeks_info': sorted_all_weeks_info}
        print(all_weeks_info)
        return render(request,
                      template_name='test.html',
                      context=ctx)


class ShowCleaningView(LoginRequiredMixin, View):
    def get(self, request):

        all_months_info = []

        for j in range(0, 12):
            single_month_info = {}
            single_month_info.update({'month': j, 'sorted_all_month_info': sorted_all_month_info[j]})
            all_months_info.append(single_month_info)


        all_days_info = []
        for i in range(1, 442):
            single_day_info = {}

            selected_cleaning = Cleaning.objects.get(week=i)
            selected_roommate = selected_cleaning.roommate
            selected_room = selected_cleaning.room


            single_day_info.update({'day': i, 'selected_roommate': selected_roommate, 'selected_room': selected_room})
            all_days_info.append(single_day_info)

        sorted_all_days_info = sorted(all_days_info, key=itemgetter('day'))

        ctx = {
            'all_months_info': all_months_info,
            'sorted_all_days_info':sorted_all_days_info}
        return render(request,
                      template_name='cleaning_result.html',
                      context=ctx)


class DeleteCleaningView(LoginRequiredMixin, View):
    def get(self, request, cleaning_id):
        cleaning = Cleaning.objects.get(id=cleaning_id)
        cleaning.delete()

        return HttpResponseRedirect('/show_cleaning')
