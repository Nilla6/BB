from django import forms
from contact.models import ContactMe

class ContactMeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter First and Last Name Here',

        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter email here',

        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Briefly describe the problem.',

        }
    ))

    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'description')
