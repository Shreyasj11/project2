from django import forms

class std_form(forms.Form):
    Name=forms.CharField()
    Age=forms.IntegerField()
    Ph_no=forms.IntegerField()
    Gender=forms.CharField()
    e_mail=forms.CharField()




