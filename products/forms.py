from django import forms
from .models import Products, Offer,Users


class Productform(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'stock', 'description', 'image_url']


class Offerform(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['code', 'description', 'discount']


class Signupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Users
        fields=['FirstName','LastName','email','username','password','PhoneNumber']


class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Users
        fields=['username','password']

class ProductSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search product name!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

