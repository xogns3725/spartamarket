from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def index(request):
    return render(request, "products/index.html")


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


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products:products")
    return redirect("products:product_detail", product.pk)


def update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/update.html", context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("products:products")


def search(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(
            title__icontains=query
        ) | Product.objects.filter(
            content__icontains=query
        ) | Product.objects.filter(
            author__username__icontains=query
        )
    else:
        results = None

    return render(request, 'products/products.html', {'results': results})


def order(request):
    order = request.GET.get('order')
    if order == 'latest':
        order_products = Product.objects.order_by('-created_at')
    else:
        order_products = Product.objects.annotate(popular=Count(
            'like_users')).order_by('-popular', '-created_at')
    return render(request, 'products/products.html', {'order_products': order_products})
