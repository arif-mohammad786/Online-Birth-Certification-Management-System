from adminuser import views
from django.urls import path
urlpatterns = [
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('viewapplication/<slug:page>/',views.viewapplication,name="viewapplication"),
    path('selectapplication/<int:id>/',views.selectapplication,name="selectapplication"),
    path('takeaction/<int:id>/',views.takeaction,name="takeaction"),
    path('adminchangepass/',views.adminchangepass,name="adminchangepass"),

]