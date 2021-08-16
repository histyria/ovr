from django.forms import ModelForm
from .models import Order
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ="__all__"
STATES = (
    ('', 'Choose...'),
    ('CA', 'California'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona')
)
 
class RegsitrationForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)