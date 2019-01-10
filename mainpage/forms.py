from django import forms
from django.forms import ModelForm
from .models import Buyer



class Checkout(ModelForm):

    class Meta:
        model = Buyer
        fields = ['firstname','lastname','email','address','zipcode']
