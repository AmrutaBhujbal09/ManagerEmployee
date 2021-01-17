# Create your models here.
#A Django model is a built in feature that django uses to create tables ,their fielld & various constraints.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Here I used python default User model ,we can extend that model using AbstractUser.


class User(AbstractUser):
    email=models.EmailField('email_address',unique=True)
    address=models.TextField(max_length=60,null=True,blank=False)
    dob=models.DateField(null=True,blank=False)
    company=models.TextField(max_length=40,null=True,blank=False)
   # status_Choice=models.CharField(max_length=10,null=True,blank=False,choices=Status_Choice,default='Active')

    #USERNAME_FIELD ='email' is uses when we want to use 'email field as the username field.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email