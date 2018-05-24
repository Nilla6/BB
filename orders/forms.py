from django import forms
from orders.models import Order
from orders.choices import *

class OrderForm(forms.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'John'

        }
    ))

    lname = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Doe'

        }
    ))

    email = forms.EmailField(widget = forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': "you@example.com"

        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': '1234 Main St'

        }
    ))

    address2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': "Apartment/Suite #"

        }
    ))

    postal_code = forms.IntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': '12345'

        }
    ))

    city = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',

        }
    ))

    state = forms.ModelChoiceField(
        queryset = Order.objects.all(),
        widget = forms.Select(
            attrs = {
                'class': 'custom-select d-block w-100'
            }
        ),
        empty_label = 'Choose a State'
    )

    country = forms.ModelChoiceField(
        queryset = Order.objects.all(),
        widget = forms.Select(
            attrs = {
                'class': 'custom-select d-block w-100'
            }
        ),
        empty_label = 'Choose a Country'
    )

    class Meta:
        model = Order
        fields = ('fname', 'lname', 'email', 'address', 'postal_code', 'city', 'state', 'country', 'stripe_id')

    
