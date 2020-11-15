from django.db import models

# Create your models here.
class admindetails(models.Model):
    aname=models.CharField(max_length=70)
    aemail=models.EmailField()
    apass=models.CharField(max_length=70)