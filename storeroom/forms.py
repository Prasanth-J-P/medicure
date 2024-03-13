from django import forms
from .models import Medicinedetails

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Medicinedetails
        fields = '__all__'



