from .models import Order, User, MethodDeliveryTable
from django import forms
from django.forms import ModelForm, TextInput, ChoiceField



class OrderForm(forms.Form):
    method_delivery = forms.ChoiceField(label="Выберете способ достваки",
                                             choices=((1, 'почта'), (2, 'транспортная компания'), (3, 'курьер')))


    method_delivery = forms.TypedChoiceField(label="Выберете способ достваки", choices=((1, 'Почта'), (2, 'Транспортная Компания'), (3, 'Курьер')))
    adress = forms.CharField(label='Ваш Адресс',widget=forms.TextInput(attrs={"placeholder": "Адресс"}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"placeholder": "Имя"}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"placeholder": "Фамилия"}))

