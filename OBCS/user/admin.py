from django.contrib import admin
from .models import User,applicationmodel
# Register your models here.
@admin.register(User)
class adminuser(admin.ModelAdmin):
    list_display=['id','fname','lname','address','phone','email','password']



@admin.register(applicationmodel)
class adminuser(admin.ModelAdmin):
    list_display=['id','dob','gender','name','birth_place','fname','permanent_address','postal_address','phone','email','doa']