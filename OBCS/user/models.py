from django.db import models
from datetime import date
# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=255)


class applicationmodel(models.Model):
    gen=(('Male','Male'),('Female','Female'))
    dob=models.DateField()
    gender=models.CharField(max_length=70,choices=gen,default="Male")
    name=models.CharField(max_length=70)
    birth_place=models.CharField(max_length=70)
    fname=models.CharField(max_length=70)
    permanent_address=models.TextField()
    postal_address=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    doa=models.DateField(default=date.today())
    status=models.CharField(max_length=70,default='Pending')
    remark=models.CharField(max_length=255,default='Application is Still Pending')
    applicant_id=models.IntegerField(null=True)

