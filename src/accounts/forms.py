from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import CustomUser

# Registration form for creating a new User with password confirmation
class UserRegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))

    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
        }
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise ValidationError("Passwords don't match.")
        return re_password

# Simple login form collecting username and password
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Phone number'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))

# Form to update profile fields stored on CustomUser
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_address', 'pincode', 'phone_number', 'profile_pic', 'date_of_birth', 'gender']
        widgets = {
            'full_address': forms.Textarea(attrs={'rows': 4}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

# Form to update basic Django User fields
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
