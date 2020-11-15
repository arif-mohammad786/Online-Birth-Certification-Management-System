from django import forms

class takeactionform(forms.Form):
    stat=(('Verified','Verified'),('Rejected','Rejected'))
    remark=forms.CharField(max_length=255,label="Admin Remarks",label_suffix=" ",
    widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    status=forms.CharField(max_length=255,label="Admin",label_suffix=" ",
    widget=forms.Select(attrs={'class':'form-control'},choices=stat))