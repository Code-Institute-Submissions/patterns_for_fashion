from django.contrib import admin
from .models import Fabric, CustomProduct

# Register your models here.


class FabricAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )


class CustomProductAdmin(admin.ModelAdmin):
    readonly_fields = ('price_custom', 'fabrics',)
    fields = ('shoulder_width', 'chest_width',
              'bust_height', 'bust_length', 'hip_circ1',
              'hip_circ2', 'back_width', 'back_length',
              'chest_circ', 'extra_info',)


admin.site.register(Fabric, FabricAdmin)
admin.site.register(CustomProduct, CustomProductAdmin)