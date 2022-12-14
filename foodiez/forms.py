from django import forms
from django.contrib.auth import get_user_model

from foodiez import models

User = get_user_model()


class Registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', "first_name", "email"]
        widgets ={
            "password": forms.PasswordInput()
        }
class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class CategoryForm(forms.ModelForm):


    class Meta:
        model = models.Category
        exclude = ["created_by"]



