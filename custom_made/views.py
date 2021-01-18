from django.shortcuts import render

from .forms import CustomProductForm


def custom_made(request):
    custom_product_form = CustomProductForm()
    template = 'custom_made/custom_made.html'
    context = {
        'custom_product_form': custom_product_form
    }

    return render(request, template, context)
