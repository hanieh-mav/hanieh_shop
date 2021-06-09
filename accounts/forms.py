from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')
    password2 = forms.CharField(widget=forms.PasswordInput, label='تکرار رمز عبور')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','phone']


    def clean_password2(self):
        cd = self.changed_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password must match')
        return cd['password2']

    def save(self , commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save() 
        return user  


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'ostan','address',]

    def clean_password(self):
        return self.initial['password']




class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)  
    password = forms.CharField(widget=forms.PasswordInput) 
   
   



class RegisterUserForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'خالی'}),label='Password')   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'خالی'}),label='Password confirmation')  
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'ostan', 'phone','zopcode', 'address', 'password')
        widgets = {
            'phone': forms.NumberInput(attrs={'placeholder': 'خالی'}, ), 
            'ostan': forms.TextInput(attrs={'placeholder': 'خالی'}, ),
            'address': forms.Textarea(attrs={'placeholder': 'خالی'}, ),
            'zipcode': forms.NumberInput(attrs={'placeholder': 'خالی'}, ),
         
        }

    def clean_ostan(self):
        ostan = self.cleaned_data['ostan']
        if ostan:
            if len(ostan) < 3 or len(ostan) > 25 or not ostan.isalpha():
                raise forms.ValidationError('یک استان معتبر وارد کنید')
        return ostan

  

    def clean_address(self):
        address = self.cleaned_data['address']
        if address:
            if len(address) < 20:
                raise forms.ValidationError('یک آدرس معتبر وارد کنید')
        return address


    def clean_zipcode(self):
        code_meli = self.cleaned_data['zipcode']
        if code_meli:
            if len(code_meli) < 10:
                raise forms.ValidationError('یک کدپستی  معتبر وارد کنید')
        return code_meli


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if len(phone) < 11:
                raise forms.ValidationError('شماره تلفن کوتاه است')
        return phone


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 3 or len(first_name) > 25 or not first_name.isalpha():
            raise forms.ValidationError('یک نام معتبر وارد کنید')
        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 3 or len(last_name) > 40 or not last_name.isalpha():
            raise forms.ValidationError('یک نام خانوادگی معتبر وارد کنید')
        return last_name