from django.forms import ModelForm
from base.models import Logement

class LogementForm(ModelForm):
    class Meta:
        model=Logement
        fields="__all__"

