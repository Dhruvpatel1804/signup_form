from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from .models import Contactmodel

class ContactForm(forms.Form):
    Firstname = forms.CharField(max_length=30)
    Lastname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    Phonenumber = forms.CharField(max_length=12)
    password = forms.CharField(max_length=8,widget=forms.PasswordInput())
    confirmpassword = forms.CharField(max_length=8,widget=forms.PasswordInput())
    pincode = forms.IntegerField(validators = [RegexValidator('^[1-9]{1}[0-9]{2}[0-9]{3}$')])

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirmpassword = cleaned_data.get('confirmpassword')
        username = cleaned_data.get('username')
        pincode = cleaned_data.get('pincode')
        Phonenumber = cleaned_data.get('Phonenumber')

        if Contactmodel.objects.filter(email=email).exists():
            raise forms.ValidationError("email already registered")
        if Contactmodel.objects.filter(Phonenumber=Phonenumber).exists():
            raise forms.ValidationError("phonenumber already registerd")
        if password != confirmpassword:
            raise forms.ValidationError("password does not match")
        
        return cleaned_data 



# firstname -
# lastname
# username - auto generated-2 letter fname - 2 lname -2 phonenum
# email  - unique
# phone num
# password  - hidden typing
# confirm password
# pincode - check valid pincode
