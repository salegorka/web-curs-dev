from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Введенные пароли не совпадают')
        return cd['password2']

from .models import Status

class StatusEditForm(forms.Form):
    all_status = list(Status.objects.all())
    choice_status = []
    for status in all_status:
        choice_status.append((status.id, status.name))
    status_field = forms.ChoiceField(choices=choice_status, label="Новый статус")


