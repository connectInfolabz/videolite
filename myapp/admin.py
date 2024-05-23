from django.contrib import admin
from .models import *
# Register your models here.


class displayUsers(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'password', 'added_on']

admin.site.register(signup, displayUsers)
