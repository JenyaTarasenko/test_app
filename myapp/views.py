from django.shortcuts import render
from .models import Product, Category



def index_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'products': products,
                                                  'categories': categories}
                  )