from django.http.response import HttpResponse
from django.shortcuts import render,redirect, HttpResponse
from user_login_app.models import User
from .models import Book,Author,Rating
from django.contrib import messages

def index(request):
    user=User.objects.get(id=request.session['user_id'])
    author=Author.objects.all()
    rating=Rating.objects.all()
    context={
        'users':user,
       ' authors':author,
       'ratings':rating
    }
    return render(request,'book_home.html',context)

def add_book(request):
    context={
        'authors':Author.objects.all()
    }
    return render(request,'add_review.html',context)

def new_b_r(request):
    user=User.objects.get(id=request.session['user_id'])
    errors = Book.objects.validator(request.POST)
    Author.objects.validator(request.POST)
    Rating.objects.validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v,extra_tags=k)
            return redirect('/dojo_reads/books/new')
    else:
        author_id=Author.objects.get(id=['author_id'])
        if author_id in Book < len :
         Author.objects.create(
         full_name=request.POST['full_name']
    )
    rating_id=Rating.objects.get(id=['rating_id'])
    if  rating_id in Book  < len:
        rating_id ==  Rating.objects.create(
        rating=request.POST['rating'],
        review=request.POST['review'],
        creator=user
    ) 
    else:
     Book.objects.create(
        title=request.POST['title'],
        creator=user,
        author=Author.objects.get(id=['author_id']),
        rating=Rating.objects.get(['rating_id'])
    )
    return redirect('/dojo_reads')

def log_out(request):
    if 'email' in request.session:
        del request.session['email']
    elif 'first_name' in request.session:
        del request.session['first_name']
    return redirect('/')