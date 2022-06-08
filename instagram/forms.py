from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image, Comment

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username','first_name','last_name','email']

class LoginUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_photo', 'bio']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
