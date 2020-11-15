from user import views
from django.urls import path
urlpatterns = [
    path('usersignup/',views.usersignup,name="usersignup"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('changepass/',views.changepass,name="changepass"),
    path('application/',views.application,name="application"),
    path('viewcertificates/',views.viewcertificates,name="viewcertificates"),
    path('selectcertificate/<int:id>/',views.selectcertificate,name="selectcertificate"),
]