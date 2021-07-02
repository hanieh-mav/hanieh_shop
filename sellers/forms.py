from django import forms
from shop.models import Product
from .models import Seller


class CustomMMCF(forms.ModelMultipleChoiceField):    
    def label_from_instance(self, member):
        return member.name


class CreateProductForm(forms.ModelForm):    
    class Meta:
        model = Seller
        fields = ('products',)  
         
        products = CustomMMCF(
            queryset=Product.objects.all(),
            widget=forms.CheckboxSelectMultiple
    )