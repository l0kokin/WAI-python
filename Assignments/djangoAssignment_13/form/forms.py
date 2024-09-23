from django import forms

class UseForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    age = forms.IntegerField(min_value=10, required=False)
    email = forms.EmailField(required=True)