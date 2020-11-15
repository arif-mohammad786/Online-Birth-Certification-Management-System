from django.contrib import admin
from .models import admindetails
# Register your models here.
@admin.register(admindetails)
class admin_details(admin.ModelAdmin):
    list_display=['id','aname','aemail','apass']