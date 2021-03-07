from django import forms

from .models import Ambulance, Institution

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = "__all__"
        exclude = ['uploaded_by',]