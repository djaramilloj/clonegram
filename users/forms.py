# Django
from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile


class ProfileForm(forms.Form):
    website = forms.URLField( max_length=200, required=True)
    bio = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    profile_pic = forms.ImageField()


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_conf = forms.CharField(max_length=70, widget=forms.PasswordInput)

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length= 80, widget=forms.EmailInput)

    # if I want to validate specific fields I must def a function like this one
    def clean_username(self):
        # username must be unique 
        username = self.cleaned_data['username']

        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('username is already in use')
        # always return de field
        return username
    
    # validation of the all the date
    def clean(self):
        # verify if password_conf match
        data = super().clean()

        password = data['password']
        password_conf = data ['password_conf']

        if password != password_conf:
            raise forms.ValidationError('Password doesn\'t match')
        return data
    
    # save user on database
    def save(self):
        # create user and profile
        data = self.cleaned_data
        data.pop('password_conf')

        user = User.objects.create_user(**data)
        profile = UserProfile(user=user)
        profile.save()

