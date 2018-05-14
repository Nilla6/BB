from django import forms

class CreationForm(forms.Form):
    post = forms.CharField()
