from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Users(models.Model):
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    profile_picture = models.ImageField(upload_to='uploads/profile_pictures')

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ), null=True, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    postmedia = models.FileField(null=True,upload_to='uploads/post_media')
    publication_date = models.DateTimeField(auto_now_add=True)
    postlocation=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.caption

class Like(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post

class Comment(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return self.tag

class Follow(models.Model):
    follower = models.ForeignKey(Users, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(Users, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.follower


# Create your models here.
