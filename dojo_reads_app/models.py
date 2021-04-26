from django.db import models
from django import forms
from django_starfield import Stars
from user_login_app.models import User



class BookManager(models.Manager):
    def validator(self,post_data):
        errors={}
        if len(post_data['title']) < 3 or len(post_data['title']) > 65:
            errors['title_length']="title must be between 3 and 65 Characters in length"
        if post_data['title']== post_data['title']:
            errors['title_unique']="Book already in the library"
        return errors

class RatingManager(models.Manager):
    def validator(self,post_data):
        errors={}
        if len(post_data['review'])< 10 or len(post_data['review'])> 400:
            errors['review_length']="Reviews must be at least 10 charcters long and less than 400 Cracters in length"
        return errors

class AuthorManager(models.Manager):
    def validator(self,post_data):
        errors={}
        if len(post_data['full_name'])<6 or len(post_data['full_name'])>80:
            errors['full_name_length']="Athor Name must be at least 6 Characters in length and no more than 80 Charaacters in length"
        if post_data['full_name']==post_data['full_name']:
            errors['full_name_unique']="Author has alredy been endtered into the system please selsect from the authors list"
        return errors


class Rating(models.Model):
    rating = models.IntegerField()
    review=models.TextField()
    creator=models.ForeignKey(User,related_name='user_rating',on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=RatingManager()

class Author(models.Model):
    full_name=models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=AuthorManager()

class Book(models.Model):
    title=models.CharField(max_length=65)
    creator=models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    author=models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    rating=models.ManyToManyField(Rating,related_name='ratings', blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= BookManager()