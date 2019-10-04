from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models

class UserRegisterForm(UserCreationForm):
    CU = 0
    OW = 1
    user_type=(
        ( CU ,'Customer'),
        ( OW ,'Owner'),
    )
    
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=user_type, label='User Type',required=False)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['house','road','city','contact','image']