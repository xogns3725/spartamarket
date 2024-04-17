from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["author", "like_users"]

        labels = {
            'title': '상품명',
            'content': '내용',
            'image': '이미지',
        }