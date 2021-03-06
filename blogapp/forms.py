from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post, MyEmail

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        }

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.email = cleaned_data['email']

            if commit:
                user.save()

            return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'password',
        }

class WritePostForm(forms.ModelForm):
    header = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Header',
        }
    ))

    image_url = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Image URL',
        }
    ))

    post_text = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Text',
        }
    ))

    class Meta:
        model = Post
        fields = {
            'image_url',
            'header',
            'post_text',
        }

class WriteEmailForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Name',
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Email',
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Subject',
        }
    ))

    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Message',
        }
    ))
    class Meta:
        model = MyEmail
        fields={
            'name',
            'email',
            'subject',
            'message',
        }




