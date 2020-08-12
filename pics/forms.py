from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pics.models import Profile, Post, Comments


class userForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        widgets = {
            'username': forms.Textarea(attrs={'class': 'input1', 'placeholder': 'username'}),
            'password1': forms.Textarea(attrs={'class': 'input2', 'placeholder': 'Password'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'username'
        self.fields['password1'].label = 'password'

        self.fields['email'].label = 'email'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_caption', 'image', 'tag_someone')
        widgets = {
            'image_caption': forms.Textarea(attrs={'class': 'input'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'comment_post')
        widgets = {
            'comment_post': forms.Textarea(attrs={'class': 'comments-input', 'placeholder': 'Add a comment'}),
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Name', 'user', 'bio']
        labels = {"profile_pic": "Change Profile Picture"}
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'input3'}),
            'Name': forms.TextInput(attrs={'class': 'input3'}),

        }


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
        labels ={
            'profile_pic':'Change Profile Picture'
        }
        widgets ={
            'profile_pic':forms.FileInput(attrs={'class':'hey'})
        }
