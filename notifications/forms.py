from datetime import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from tempus_dominus.widgets import DateTimePicker

from notifications.models import Push, Option


class PushForm(forms.ModelForm):
    class Meta:
        model = Push
        fields = ['title', 'text', 'pushed_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите заголовок'}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Введите текст уведомления'}),
            'pushed_at': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                    'minDate': datetime.date(datetime.now()).strftime('%Y-%m-%d'),
                },
                attrs={
                    'icon_toggle': True,
                }
            )
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите название'})
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
