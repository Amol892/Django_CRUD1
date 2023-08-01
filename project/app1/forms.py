from django import forms 
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'
        
        widgets={
            'DOB':forms.DateInput(attrs={"type":'date'})
        }