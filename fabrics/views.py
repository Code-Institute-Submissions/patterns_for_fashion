from django.shortcuts import render
from .models import Fabric

# Create your views here.


def view_fabrics(request):
    """" A view to view the available fabrics """

    fabrics = Fabric.objects.all()

    context = {
        'fabrics': fabrics,
    }

    return render(request, context)
