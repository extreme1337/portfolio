from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    nationality = models.CharField(max_length=30)
    freelance =  models.CharField(max_length=30, default="Available")
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email =models.EmailField(max_length=50)
    skype = models.CharField(max_length=30)
    languages = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    
