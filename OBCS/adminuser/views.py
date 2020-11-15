from django.shortcuts import render,HttpResponseRedirect
from .models import admindetails
from user.forms import loginform,changepassform
from django.db.models import Q
from django.contrib import messages
from user.models import applicationmodel
from .forms import takeactionform
# Create your views here.
def adminlogin(request):
    if request.session.get('is_admin_login',False)==True:
        return HttpResponseRedirect('/admin/dashboard/')
    else:
        if request.method=="POST":
            fm=loginform(request.POST)
            if fm.is_valid():
                admin_eml=fm.cleaned_data['email']
                admin_pwd=fm.cleaned_data['password']
                pi=admindetails.objects.filter(Q(aemail=admin_eml) & Q(apass=admin_pwd))
                if((pi.count())>0):
                    usr=pi[:1].get()
                    request.session['is_admin_login']=True
                    request.session['adminemail']=usr.aemail
                    request.session['adminname']=usr.aname
                    return HttpResponseRedirect('/admin/dashboard')
                else:
                    messages.warning(request,'You Have Entered Wrong Password Or Email ID !!')
        else:
            fm=loginform()
    
    return render(request,'adminuser/adminlogin.html',{'form':fm})



def dashboard(request):
    if request.session.get('is_admin_login',False)==True:
        new=applicationmodel.objects.filter(status='Pending')
        verified=applicationmodel.objects.filter(status='Verified')
        rejected=applicationmodel.objects.filter(status='Rejected')
        return render(request,'adminuser/dashboard.html',{'new':new.count(),'verified':verified.count(),'rejected':rejected.count(),
        'name':request.session['adminname'],'email':request.session['adminemail']})
    else:
        return HttpResponseRedirect('/admin/adminlogin/')



def viewapplication(request,page):
    if request.session.get('is_admin_login',False)==True:
        if page=='New':
            applications=applicationmodel.objects.filter(status="Pending")
        elif page=='Verified':
            applications=applicationmodel.objects.filter(status="Verified")
        else:
            applications=applicationmodel.objects.filter(status="Rejected")
        return render(request,'adminuser/viewapplication.html',{'applications':applications,'page':page,'name':request.session['adminname'],'email':request.session['adminemail']})
    else:
        return HttpResponseRedirect('/admin/adminlogin/')



def selectapplication(request,id):
    if request.session.get('is_admin_login',False)==True:
        application=applicationmodel.objects.get(pk=id)
        return render(request,'adminuser/selectapplication.html',{'application':application,'name':request.session['adminname'],'email':request.session['adminemail']})
    else:
        return HttpResponseRedirect('/admin/adminlogin/')



def takeaction(request,id):
    if request.session.get('is_admin_login',False)==True:
        if request.method=="POST":
            fm=takeactionform(request.POST)
            if fm.is_valid():
                pi=applicationmodel.objects.get(pk=id)
                pi.remark=fm.cleaned_data['remark']
                pi.status=fm.cleaned_data['status']
                pi.save()
                messages.success(request,'Application Remarked Successfully !!!')
        else:
            fm=takeactionform()
        return render(request,'adminuser/takeaction.html',{'form':fm,'name':request.session['adminname'],'email':request.session['adminemail']})
    else:
        return HttpResponseRedirect('/admin/adminlogin/')


def adminchangepass(request):
    if request.session.get('is_admin_login',False)==True:
        if request.method=="POST":
            fm=changepassform(request.POST)
            if fm.is_valid():
                pi=admindetails.objects.get(aemail=request.session['adminemail'])
                pi.apass=fm.cleaned_data['new_pass']
                pi.save()
                messages.success(request,'Password Changed Successfully !!!')
        else:
            fm=changepassform()
        fm.fields['email'].initial=request.session['adminemail']
        return render(request,'adminuser/changepass.html',{'form':fm,'name':request.session['adminname'],'email':request.session['adminemail']})
    else:
        return HttpResponseRedirect('/admin/adminlogin/')