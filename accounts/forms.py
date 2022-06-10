from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserChangeForm(UserChangeForm):

    # password = None

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
        }
