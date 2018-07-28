from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_description', 'video'] 