from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from owner.models import Order

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["product","address","phone_number"]

        widgets={
            "product":forms.Select(attrs={"class":"form-control","readonly":True}),
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
        }


