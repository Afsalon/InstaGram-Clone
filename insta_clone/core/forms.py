from django import forms
from django.contrib.auth import get_user_model
from core.models import Post
class EditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'username','email','profile_pic','website','bio','phone_number','gender')
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post','caption')
