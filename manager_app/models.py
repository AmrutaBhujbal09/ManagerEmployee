

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    Status_Choice=(
        ('ACTIVE','Active'),
        ('INACTIVE','Inactive')
    )



    email=models.EmailField('email_address',unique=True)
    #contact_number=models.TextField(max_length=10,null=True)
    #by default null valuse is false means its mandetory to provide a value,blank=false
    address=models.TextField(max_length=60,null=True,blank=False)
    dob=models.DateField(null=True,blank=False)
    company=models.TextField(max_length=40,null=True,blank=False)
    status_Choice=models.CharField(max_length=10,null=True,blank=False,choices=Status_Choice,default='Active')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email