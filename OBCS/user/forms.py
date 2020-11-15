from django import forms
from .models import User,applicationmodel
from datetime import date

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['fname','lname','address','phone','email','password']
        labels={
            'fname':'First Name','lname':'Last Name','address':'Address','phone':'Phone Number','email':'Email',
            'password':'Password'
        }
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    
class loginform(forms.Form):
    email=forms.CharField(required=True,label="Email",max_length=70,
    widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(required=True,label="Password",max_length=70,
    widget=forms.PasswordInput(attrs={'class':'form-control'}))


class changepassform(forms.Form):
    email=forms.CharField(required=False,disabled=True,max_length=70,label="Email"
    ,widget=forms.EmailInput(attrs={'class':'form-control'}))
    new_pass=forms.CharField(max_length=70,label="New Password",
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
   

class applicationform(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(applicationform,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=applicationmodel
        #fields="__all__"
        exclude=('doa','status','remark',)
        labels={
            'gen':'Gender','dob':'Date Of Birth','name':'Full Name','birth_place':'Birth Place','fname':'Father Name',
            'permanent_address':'Permanent Address','postal_address':'Postal Address','phone':'Mobile Number',
            'email':'Email ID','applicant_id':' '
        }
        
        widgets={
            'gen':forms.Select(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'birth_place':forms.TextInput(attrs={'class':'form-control'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'permanent_address':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'postal_address':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'applicant_id':forms.HiddenInput(),
        }
