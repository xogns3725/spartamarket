from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    price = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="ProductLike", related_name="like_products"
    )
    
    def __str__(self):
        return self.title


class ProductLike(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
