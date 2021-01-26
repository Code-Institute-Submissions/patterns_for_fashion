from django.contrib import admin
from .models import CustomProduct

# Register your models here.


class CustomProductAdmin(admin.ModelAdmin):
    fields = ('shoulder_width', 'chest_width',
              'bust_height', 'bust_length', 'hip_circ1',
              'hip_circ2', 'back_width', 'back_length',
              'chest_circ', 'extra_info',)


admin.site.register(CustomProduct, CustomProductAdmin)
