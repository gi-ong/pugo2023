from .models import Short
from django import forms

class ShortForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = (
            "full_url",
        )
