from django import forms
from website.models import Product

class CreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Description of Product',

        }
    ))

    price = forms.DecimalField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Price of Product',
        }
    ))

    quantity = forms.PositiveIntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'How many do you have to sell',
        }
    ))

    image = forms.ImageField()

    class Meta:
        model = Product
        fields = ('description', 'price', 'quantity', 'image')
