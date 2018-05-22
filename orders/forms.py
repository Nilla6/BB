from django import forms
from orders.models import Order

class OrderForm(form.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'First Name',

        }
    ))

    lname = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Last Name',

        }
    ))

    email = forms.EmailField(widget = forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Email',
        }
    ))

    address = description = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Address',

        }
    ))

    postal_code = forms.IntegerField(widget = forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Zip Code',
        }
    ))

    city = description = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'City',

        }
    ))

    class Meta:
        model = Order
        fields = ('fname', 'lname', 'email', 'address', 'postal_code', 'city')
