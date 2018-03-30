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

from roommates_app.views import (AddApartmentView, ShowApartmensView,
                                 AddRoommatetView, ShowRoommatedView, DeleteRoommateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowApartmensView.as_view(), name='show-apartment'),
    path('add_apartment', AddApartmentView.as_view(), name='add-apartment'),
    path('show_apartment', ShowApartmensView.as_view(), name='show-apartment'),
    path('add_roommate', AddRoommatetView.as_view(), name='add-roommate'),
    path('show_roommate', ShowRoommatedView.as_view(), name='show-roommate'),
    path('delete_roommate/<int:roommate_id>', DeleteRoommateView.as_view(), name='delete-roommate')
]
