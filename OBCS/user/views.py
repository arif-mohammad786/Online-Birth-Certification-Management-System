from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform,loginform,changepassform,applicationform
from django.contrib import messages
from .models import User,applicationmodel
from django.db.models import Q
# Create your views here.
def usersignup(request):
    if request.session.get('is_login',False)==True:
        return HttpResponseRedirect('/user/dashboard/')
    else:
        if request.method=="POST":
            fm=signupform(request.POST)
            if fm.is_valid():
                eml=fm.cleaned_data['email']
                pi=User.objects.filter(email=eml)
                if pi.count()>0:
                    messages.warning(request,'Try With Different Email ID !!')
                else:
                    fm.save()
                    messages.success(request,'Signed Up Successfully !!')
                    fm=signupform()
        else:
            fm=signupform()
    return render(request,'user/usersignup.html',{'form':fm})

def userlogin(request):
    if request.session.get('is_login',False)==True:
        return HttpResponseRedirect('/user/dashboard/')
    else:
        if request.method=="POST":
            fm=loginform(request.POST)
            if fm.is_valid():
                eml=fm.cleaned_data['email']
                pwd=fm.cleaned_data['password']
                pi=User.objects.filter(Q(email=eml) & Q(password=pwd))
                if((pi.count())>0):
                    usr=pi[:1].get()
                    request.session['is_login']=True
                    request.session['useremail']=usr.email
                    request.session['fname']=usr.fname
                    request.session['lname']=usr.lname
                    return HttpResponseRedirect('/user/dashboard')
                else:
                    messages.warning(request,'You Have Entered Wrong Password Or Email ID !!')
        else:
            fm=loginform()
    
    return render(request,'user/userlogin.html',{'form':fm})

def dashboard(request):
    if request.session.get('is_login',False)==True:
        fname=request.session['fname']
        lname=request.session['lname']
        useremail=request.session['useremail']
        return render(request,'user/dashboard.html',{'fname':fname,'lname':lname,'useremail':useremail})
    else:
        return HttpResponseRedirect('/user/userlogin/')



def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')



def userprofile(request):
    if request.session.get('is_login',False)==True:
        fname=request.session['fname']
        lname=request.session['lname']
        useremail=request.session['useremail']
        pi=User.objects.get(email=useremail)
        if request.method=="POST":
            fm=signupform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile Edited Successfully !!!')
        else:
            fm=signupform(instance=pi)
        return render(request,'user/userprofile.html',{'fname':fname,'lname':lname,'useremail':useremail,'form':fm})
    else:
        return HttpResponseRedirect('/user/userlogin/')


def changepass(request):
    if request.session.get('is_login',False)==True:
        fname=request.session['fname']
        lname=request.session['lname']
        useremail=request.session['useremail']
        if request.method=="POST":
            fm=changepassform(request.POST)
            if fm.is_valid():
                pi=User.objects.get(email=request.session['useremail'])
                pi.password=fm.cleaned_data['new_pass']
                pi.save()
                messages.success(request,'Password Changed Successfully !!!')
        else:
            fm=changepassform()
        fm.fields['email'].initial=request.session['useremail']
        return render(request,'user/changepass.html',{'fname':fname,'lname':lname,'useremail':useremail,'form':fm})
    else:
        return HttpResponseRedirect('/user/userlogin/')

def application(request):
    if request.session.get('is_login',False)==True:
        fname=request.session['fname']
        lname=request.session['lname']
        useremail=request.session['useremail']
        if request.method=="POST":
            fm=applicationform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Application Submitted Successfully !!!')
        else:
            fm=applicationform()
            pi=User.objects.get(email=request.session['useremail'])
            fm.fields['applicant_id'].initial=pi.id
        return render(request,'user/application.html',{'fname':fname,'lname':lname,'useremail':useremail,'form':fm})
    else:
        return HttpResponseRedirect('/user/userlogin/')
    
def viewcertificates(request):
    if request.session.get('is_login',False)==True:
        pi=User.objects.get(email=request.session['useremail'])
        certificates=applicationmodel.objects.filter(applicant_id=pi.id)
        return render(request,'user/viewcertificates.html',{'certificates':certificates,'fname':request.session['fname'],
        'lname':request.session['lname'],'useremail':request.session['useremail']})
    else:
        return HttpResponseRedirect('/user/userlogin/')



def selectcertificate(request,id):
    if request.session.get('is_login',False)==True:
        certificate=applicationmodel.objects.get(pk=id)
        return render(request,'user/selectcertificate.html',{'certificate':certificate,'fname':request.session['fname'],
        'lname':request.session['lname'],'useremail':request.session['useremail']})
    else:
        return HttpResponseRedirect('/user/userlogin/')