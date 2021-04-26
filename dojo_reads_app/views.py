
from django.shortcuts import render,redirect, HttpResponse
from user_login_app.models import User
from .models import Book,Author,Rating
from django.contrib import messages

def index(request):
    print(request.session['user_id'])
    user=User.objects.get(id=request.session['user_id'])
    # printing user id   
    print('*****************************')
    print(user.id)
    
    author=Author.objects.all()
    rating=Rating.objects.all()
    context={
        'user':user,
       'authors':author,
       'ratings':rating
    }
    return render(request,'book_home.html',context)

def add_book(request):
    context={
        'authors':Author.objects.all()
    }
    return render(request,'add_review.html',context)

def new_b_r(request):
    # user=User.objects.get(id=request.session['user_id'])
    # errors = Book.objects.validator(request.POST)
    # Author.objects.validator(request.POST)
    # Rating.objects.validator(request.POST)
    # if errors:
    #     for k, v in errors.items():
    #         messages.error(request, v,extra_tags=k)
    #         return redirect('/dojo_reads/books/new')
    # else:
    #     author_id=Author.objects.get(id=['author_id'])
    #     if author_id in Book < len :
    #      Author.objects.create(
    #      full_name=request.POST['full_name']
    # )
    # rating_id=Rating.objects.get(id=['rating_id'])
    # if  rating_id in Book  < len:
    #     rating_id ==  Rating.objects.create(
    #     rating=request.POST['rating'],
    #     review=request.POST['review'],
    #     creator=user
    # ) 
    # else:
    #  Book.objects.create(
    #     title=request.POST['title'],
    #     creator=user,
    #     author=Author.objects.get(id=['author_id']),
    #     rating=Rating.objects.get(['rating_id'])
    # )
    return redirect('/dojo_reads')

def log_out(request):
   request.session.flush()
   return redirect('/')

def process(request):
    errors = Book.objects.validator(request.POST)
    Author.objects.validator(request.POST)
    Rating.objects.validator(request.POST)
    Book.objects.validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v,extra_tags=k)
            return redirect('/dojo_reads/books/new')
    else:
        try:
            author = request.POST['author']
        except:
            author = ''
    try:
        full_name = request.POST['full_name']
    except:
        full_name = ''
    # Author Check / Create
    if author.isnumeric():
        author_obj = Author.objects.get(id=author)
        print(author_obj.full_name)
    try:
        rating = request.POST['rating'],
        review= request.POST['review'],
        creator= request.session['user_id']
    except:
        rating = ''
        review =''
        creator =''
    try:
        rating = request.POST['rating']
        review = request.POST['review']
        creator=request.POST['user_id']
    except:
        rating = ''
        review =''
        creator=''
    # Rating Check / Create
    if rating.isnumeric():
       rating_obj = Rating.objects.get(id=rating)
       print(rating_obj.rating,rating_obj.review,rating_obj.creator)
    try:
        book=request.POST['book'],
        user=User.objects['user_id'],
        title = request.POST['title'],
        author= request.session['author'],
        creator= user,
        rating=request.POST['rating']
    except:
        title = ''
        author =''
        creator =''
        rating=''
    try:
        title= request.POST['title'],
        author = request.POST['author'],
        creator=user,
        rating=rating
    except:
       title = ''
       author =''
       creator=''
       rating=''
    # Rating Check / Create
    if Book.isnumeric():
       book_obj = Book.objects.get(id=book)
       print(book_obj.title,book_obj.author,book_obj.creator,book_obj.rating)
    else:
        new_book=Book(title=title,author=author,rating=rating,creator=user)
        new_book.save()
        print(new_book)
        new_author=Author(full_name=full_name)
        new_author.save()
        print(new_author)
        new_rating = Rating(rating=rating,review=review,creator=creator)
        new_rating.save()
        print(new_rating)
    # Book Check / Create
    return redirect('/dojo_reads/books/new')