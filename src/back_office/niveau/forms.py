from django.forms import ModelForm
from base.models import Niveau

class NiveauForm(ModelForm):
    class Meta:
        model=Niveau
        fields = "__all__" 