from django import forms
from .models import CustomProduct


class CustomProductForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        readonly_fields = ('price_custom', 'fabrics',)
        fields = ('shoulder_width', 'chest_width',
                  'bust_height', 'bust_length', 'hip_circ1',
                  'hip_circ2', 'back_width', 'back_length',
                  'chest_circ', 'extra_info',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
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

        self.fields['shoulder_width'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 custom-made-form-input'
            self.fields[field].label = False
