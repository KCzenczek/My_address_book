from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    login = forms.CharField(max_length=24)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(
            username=cleaned_data['login'],
            password=cleaned_data['password'],
        )

        if user is None:
            raise forms.ValidationError('Invalid login or password')

        self.user = user

        return cleaned_data
