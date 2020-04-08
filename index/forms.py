from django.forms import ModelForm
from .models import Covid

class CreateForm(ModelForm):
    class Meta:
        model = Covid
        fields = ('__all__')
