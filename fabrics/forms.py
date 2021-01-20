from django import forms
from .widgets import CustomClearableFileInput
from .models import Fabric


class FabricForm(forms.ModelForm):

    class Meta:
        model = Fabric
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fabrics = Fabric.objects.all()
        friendly_names =[(c.id, c.get_friendly_name()) for c in fabrics]

        self.fields['fabric'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
