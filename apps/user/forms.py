from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User    
        fields = (
            'username',
            'phone',
            'email',
            'address',
            'brief_description',
            'photo',
            'password',
        )
        widgets = {
            'username': forms.TextInput(attrs={'class':'form__input', 'placeholder':'Имя пользователя'}),
            'phone': forms.TextInput(attrs={'class':'form__input', 'placeholder':'Номер телефона'}),
            'email': forms.EmailInput(attrs={'class':'form__input', 'placeholder':'Email (необязательно)'}),
            'address': forms.TextInput(attrs={'class':'form__input', 'placeholder':'Адрес (необязательно)'}),
            'brief_description': forms.TextInput(attrs={'class':'form__input', 'placeholder':'Краткое описание (необязательно)'}),
            'password': forms.PasswordInput(attrs={'class':'form__input', 'placeholder':'Пароль'}),
            'photo': forms.FileInput(attrs={'class':'form__input form__input-file'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form__input', 'placeholder':'Имя пользователя'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':'Пароль'}))
    