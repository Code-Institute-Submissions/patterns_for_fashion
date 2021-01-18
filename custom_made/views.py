from django.shortcuts import render

from custom_made.forms import CustomProductForm


def custom_made_view(request):
    custom_product_form = CustomProductForm()
    template = 'custom_made/custom_made.html'
    context = {
        'custom_product_form': custom_product_form
    }

    return render(request, template, context)
