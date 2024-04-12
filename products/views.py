from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, "products/index.html")

# 상품페이지
def products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)