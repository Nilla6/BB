from django import forms
from website.models import Products

class CreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Description of Product',

        }
    ))
    price = forms.FloatField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Price of Product',
        }
    ))
    quantity = forms.IntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'How many do you have to sell',
        }
    ))

    image = forms.ImageField()

    class Meta:
        model = Products
        fields = ('description', 'price', 'quantity', 'image')
