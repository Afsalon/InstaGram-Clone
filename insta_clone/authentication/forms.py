from django import forms
from user.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm




class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields=('email','full_name','username', 'password')

        help_texts = {
            'username': None,
        }
        widgets = {
            'email':forms.EmailInput(attrs={'class':'input','placeholder':'Email'}),
            'full_name':forms.TextInput(attrs={'class':'input','placeholder':'Full Name'}),
            'username':forms.TextInput(attrs={'class':'input','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'input','placeholder':'Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = ""
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password'].label = ""

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= User
        fields=('email','full_name','username','profile_pic')
