
# Create your models here.

from django.db import models
from manager_app.models import User



class Employee(models.Model):

    Status_Choice=(
        ('ACTIVE','Active'),
        ('INACTIVE','Inactive')
    )



    email=models.EmailField('email_address',unique=True)
    first_name=models.CharField(max_length=50,blank=False,null=True,default='kiran')
    last_name=models.CharField(max_length=50,blank=False,null=True)
    # by default null valuse is false means its mandetory to provide a value,blank=false
    address=models.TextField(max_length=60,null=True,blank=False)
    dob=models.DateField(null=True,blank=False)
    company=models.TextField(max_length=40,null=True,blank=False)
    user_id = models.ForeignKey(User,null=False,blank=False, on_delete=models.CASCADE)
    mobile=models.TextField(max_length=10,null=True)
    city=models.TextField(max_length=10,null=True)
    password=models.CharField(max_length=50,default='kiran')
    Status_Choice=models.CharField(max_length=10,null=True,blank=False,choices=Status_Choice,default='Active')

