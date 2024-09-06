from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ChefSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_chef = True  # Custom flag to differentiate chefs
        if commit:
            user.save()
        return user

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_chef = False  # Custom flag to differentiate regular users
        if commit:
            user.save()
        return user
