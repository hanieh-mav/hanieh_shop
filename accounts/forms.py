from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import fields
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
   
   

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'required': 'true' }),label='گذرواژه')   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'required': 'true' }),label=' تکرار گذرواژه  ') 
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'ostan', 'phone','zipcode', 'address', 'password1','password2')
        widgets = {
            'phone': forms.TextInput(attrs={ 'required': 'true' }), 
            'ostan': forms.TextInput(attrs={ 'required': 'true' }),
            'address': forms.Textarea(attrs={ 'required': 'true' }),
            'zipcode': forms.TextInput(attrs={ 'required': 'true' }),
        }
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('ایمیل نامعتبر است')
        return email

        

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password must match')
        return cd['password2']



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
        zipcode = self.cleaned_data['zipcode']
        zipcode = str(zipcode)
        if zipcode:
            if len(zipcode) < 10:
                raise forms.ValidationError('یک کدپستی  معتبر وارد کنید')
        return zipcode



    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if len(phone) < 11 or User.objects.filter(phone=phone).exists():
                raise forms.ValidationError('شماره تلفن نامعتبر است')
        return phone


class ChangeDetailuserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'ostan', 'phone','zipcode', 'address',)


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
        zipcode = self.cleaned_data['zipcode']
        zipcode = str(zipcode)
        if zipcode:
            if len(zipcode) < 10:
                raise forms.ValidationError('یک کدپستی  معتبر وارد کنید')
        return zipcode



    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if len(phone) < 11 or User.objects.filter(phone=phone).exists():
                raise forms.ValidationError('شماره تلفن نامعتبر است')
        return phone

