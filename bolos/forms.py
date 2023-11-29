from django.forms import ModelForm
from .models import Bolo, Item


class BoloForm(ModelForm):
   
    class Meta:
        model=Bolo
        fields='__all__'

class ItemForm(ModelForm):

    class Meta:
        model=Item
        fields='__all__'       