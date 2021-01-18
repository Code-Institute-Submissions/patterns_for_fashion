from django import forms
from .models import CustomProduct


class CustomProductForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        fields = ('shoulder_width', 'chest_width',
             'bust_height', 'bust_length', 'hip_circ1',
             'hip_circ2', 'back_width', 'back_length',
             'chest_circ', 'extra_info',)
