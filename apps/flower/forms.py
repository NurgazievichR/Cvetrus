from django import forms

from apps.settings.models import Setting

setting = Setting.objects.latest('id')

class AddBalanceForm(forms.Form):
    amount = forms.IntegerField(max_value=10000, widget=forms.NumberInput(attrs={'name':'amount', 'class':'add__form-input', 'placeholder':'1 000, 00 Р'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'name':'phone', 'class':'add__form-input', 'value':'+996','type':'tel','placeholder':f'{setting.phone}'}))
