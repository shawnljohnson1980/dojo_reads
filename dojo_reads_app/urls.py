from . import views
from django.urls import path

urlpatterns=[
path('',views.index),
path('/books/new',views.add_book),
path('/book/new',views.new_b_r),
path('',views.log_out),

]