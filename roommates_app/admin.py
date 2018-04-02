from django.contrib import admin

from .models import (Roommate, Room, Cleaning)

# Register your models here.

admin.site.register(Roommate)
admin.site.register(Room)
admin.site.register(Cleaning)
