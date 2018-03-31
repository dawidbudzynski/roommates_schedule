"""roommates_schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from roommates_app.views import (AddAccountView, ShowAccountView, DeleteAccountView,
                                 AddRoommateView, ShowRoommatesView, DeleteRoommateView,
                                 AddRoomView, ShowRoomsView, DeleteRoomView,
                                 LoginToApartmentView, LogoutView,
                                 AddCleaningView, ShowCleaningView, DeleteCleaningView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowAccountView.as_view(), name='show-apartment'),
    path('add_account', AddAccountView.as_view(), name='add-account'),
    path('show_account', ShowAccountView.as_view(), name='show-account'),
    path('delete_user/<int:user_id>', DeleteAccountView.as_view(), name='delete-user'),
    path('add_roommate', AddRoommateView.as_view(), name='add-roommate'),
    path('show_roommate', ShowRoommatesView.as_view(), name='show-roommate'),
    path('delete_roommate/<int:roommate_id>', DeleteRoommateView.as_view(), name='delete-roommate'),
    path('add_room', AddRoomView.as_view(), name='add-room'),
    path('show_room', ShowRoomsView.as_view(), name='show-room'),
    path('delete_room/<int:room_id>', DeleteRoomView.as_view(), name='delete-room'),
    path('login', LoginToApartmentView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('add_cleaning', AddCleaningView.as_view(), name='add-cleaning'),
    path('show_cleaning', ShowCleaningView.as_view(), name='show-cleaning'),
    path('delete_cleaning/<int:cleaning_id>', DeleteCleaningView.as_view(), name='delete-cleaning'),
]

