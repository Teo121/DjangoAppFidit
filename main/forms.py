from django import forms
from .models import Rezervacija

class RezervacijaForm(forms.ModelForm):
    class Meta:
        model = Rezervacija
        fields = ['korisnik', 'smjestaj', 'datum_dolaska', 'datum_odlaska', 'broj_gostiju']
        widgets = {
            'datum_dolaska': forms.DateInput(attrs={'type': 'date'}),
            'datum_odlaska': forms.DateInput(attrs={'type': 'date'}),
        }
