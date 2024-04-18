from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    Form for user registration, extends UserCreationForm.
    Allows users to register with username, email, and password.
    """
    email = forms.EmailField()

    class Meta:
        """
        Meta class containing model and fields information.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user information.
    Allows users to update their username and email.
    """
    email = forms.EmailField()

    class Meta:
        """
        Meta class containing model and fields information.
        """
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    Allows users to update their profile image.
    """
    class Meta:
        """
        Meta class containing model and fields information.
        """
        model = Profile
        fields = ['image']