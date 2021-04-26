from django.contrib import admin

# Register your models here.
from .models import Book,Author,Rating
from user_login_app.models import User
admin.site.register([ Book,Author,Rating,User])