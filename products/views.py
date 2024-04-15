from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, "products/index.html")

# 상품페이지
def products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)

# 상품 상세페이지
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)

# 상품 등록페이지
# @login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            # product.author = request.user
            product.save()
            return redirect("products:product_detail", product.id)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)