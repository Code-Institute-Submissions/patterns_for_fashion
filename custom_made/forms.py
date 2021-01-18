from django import forms
from .models import CustomProduct


class CustomProductForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        fields = ('shoulder_width', 'chest_width',
             'bust_height', 'bust_length', 'hip_circ1',
             'hip_circ2', 'back_width', 'back_length',
             'chest_circ', 'extra_info',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'shoulder_width': 'Shoulder Width',
            'chest_width': 'Chest Width',
            'bust_height': 'Bust Height',
            'bust_length': 'Bust Length',
            'hip_circ1': 'Hip Circumference 1',
            'hip_circ2': 'Hip Circumference 2',
            'back_width': 'Back Width',
            'back_length': 'Back Length',
            'chest_circ': 'Chest Circumference',
            'extra_info': 'Other Comments',
        }

        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
