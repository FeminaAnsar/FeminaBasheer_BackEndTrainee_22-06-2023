from django.db import models
from distutils.command.upload import upload
from django.db.models import (
    CharField,
    EmailField,
    IntegerField,
    TextField,
    FileField,
    ImageField
)

class Student(models.Model):
    admissionNo=CharField(max_length=100)
    fullName=CharField(max_length=100)
    email=EmailField(max_length=100)
    age=IntegerField()
    class_Student=IntegerField()
    description=TextField()
    image=ImageField(upload_to="media/images",null=True,blank=True)
    markList=FileField(upload_to="media/files",null=True,blank=True)

    def __str__(self):
        return self.fullName

# Create your models here.
