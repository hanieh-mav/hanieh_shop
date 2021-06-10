from django import forms
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'email': forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع پیام'}),
            'text': forms.TextInput(attrs={'placeholder': 'متن پیام'}),
        }