from django import forms


class profNameForm(forms.Form):
    name = forms.CharField()