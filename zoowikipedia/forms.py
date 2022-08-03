from django import forms
from django.core.exceptions import ValidationError

from .models import *

# Форма заполнения информации для класса Classis
class AddClassisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Classis
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # Валидатор для поля name класса Classis
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) > 200:
    #         raise ValidationError('Длина превышает 200 символов')
    #
    #     return name

# Форма заполнения информации для класса Ordo
class AddOrdoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classis'].empty_label = "Категория не выбрана"

    class Meta:
        model = Ordo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
