from django.shortcuts import render
from django.template.loader import get_template
from ecommerce.models import Product  # Make sure you have the correct import for your Product model

def product_list(request):
    products = Product.objects.all()  # Replace with your actual product retrieval logic
    template = get_template('ecommerce/product_list.html')
    context = {'products': products}
    rendered_template = template.render(context)
    return render(request, None, {'rendered_template': rendered_template})
