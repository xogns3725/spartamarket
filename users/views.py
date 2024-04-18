from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from products.models import Product
from accounts.models import User

def users(request):
    return render(request, "users/users.html")


def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    liked_products = Product.objects.filter(like_users=user)
    profile_image = User.objects.filter(username=username)
    context = {
        "user": user,
        'liked_products': liked_products,
        'profile_image' : profile_image
    }
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if request.user != member:
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")


@require_POST
def unlike(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        product.like_users.remove(request.user)
        return redirect('users:profile', username=request.user.username)
    else:
        return redirect("accounts:login")

