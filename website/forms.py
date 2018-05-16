from django import forms
from website.models import Products

class CreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Description of Product'

        }
    ))
    price = forms.FloatField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control'
        }
    ))
    quantity = forms.IntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Products
        fields = ('description', 'price', 'quantity')
