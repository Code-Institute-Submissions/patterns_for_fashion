from django.shortcuts import render

from custom_made.forms import CustomProductForm
from fabrics.models import Fabric
from products.models import Product


def custom_made_view(request):
    products = Product.objects.only('price_custom', 'name')
    fabrics = Fabric.objects.all()
    custom_product_form = CustomProductForm()
    template = 'custom_made/custom_made.html'
    context = {
        'products': products,
        'fabrics': fabrics,
        'custom_product_form': custom_product_form
    }

    return render(request, template, context)
