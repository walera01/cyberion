from django import forms
from .models import *

class RegisterDrugs(forms.ModelForm):
    class Meta:
        model = Drugs
        exclude = [""]
