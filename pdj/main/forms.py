from django import forms
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import ModelForm

class FormZap(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(attrs={'class': 'form-input', 'placeholder': 'Enter phone number'})
    )

    city_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]*$',
        message='City should only contain letters a-z.',
        code='invalid_city'
    )

    city = forms.CharField(max_length=255, validators=[city_validator],
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'City'}))

    class Meta:
        model = ModelForm
        fields = ['name', 'phone_number', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'tel', 'class': 'form-input', 'placeholder': 'Name'}),
        }