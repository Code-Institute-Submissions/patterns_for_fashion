from django.shortcuts import render, get_object_or_404
from custom_made.forms import CustomProductForm
from fabrics.models import Fabric
from products.models import Product


def custom_made_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    fabrics = Fabric.objects.all()
    custom_product_form = CustomProductForm()
    template = 'custom_made/custom_made.html'
    context = {
        'product': product,
        'fabrics': fabrics,
        'custom_product_form': custom_product_form
    }

    return render(request, template, context)
