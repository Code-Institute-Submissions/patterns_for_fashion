from django.contrib import admin
from .models import Fabric


class FabricAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'image_url',
        'image',
    )

    ordering = ('name',)


admin.site.register(Fabric, FabricAdmin)
