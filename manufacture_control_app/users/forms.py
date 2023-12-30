from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name', 'user_id', 'username']
        field_classes = {
            'username': UsernameField
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name',
            }),
        }


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email']
