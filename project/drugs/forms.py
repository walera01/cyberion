from django import forms
from .models import *

class RegisterDrugs(forms.ModelForm):
    class Meta:
        drugs=Drugs
