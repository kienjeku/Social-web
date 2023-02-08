from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['first_name', 'last_name','email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['avatar', 'bio']