from django.db import models
from django.db.models import (
    CharField,
    DateField,
    BooleanField,
    TextField,
    DecimalField,
    EmailField,
    ForeignKey,
    ManyToManyField
)

class Author(models.Model):
    name=CharField(max_length=100)
    birthday=DateField()
    email=EmailField(max_length=255)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name=CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = CharField(max_length=100)
    author = ForeignKey(Author,on_delete=models.CASCADE)
    publicationDate = DateField()
    createdDate = DateField(auto_now_add=True)
    isAvailable =BooleanField(default=True)
    price = DecimalField(max_digits=8,decimal_places=2)
    description = TextField(default=True)
    bookCode =CharField(max_length=25)
    category = ForeignKey(Category,on_delete=models.CASCADE)
    genre =ManyToManyField(Genre)
    rating =DecimalField(max_digits=3,decimal_places=1)
    def __str__(self):
        return self.title
# Create your models here.
