from django.contrib import admin
from .models import Fabric

# Register your models here.


class FabricAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )


admin.site.register(Fabric, FabricAdmin)
