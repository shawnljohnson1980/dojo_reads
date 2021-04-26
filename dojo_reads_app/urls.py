from . import views
from django.urls import path

urlpatterns=[
path('',views.index),
path('/books/new',views.add_book),
path('/book/new',views.process),
path('',views.log_out),
]