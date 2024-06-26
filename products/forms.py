from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    hashtags = forms.CharField(label='해시태그', widget=forms.Textarea, required=False)
    
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["author", "like_users"]

        labels = {
            'title': '상품명',
            'content': '내용',
            'image': '이미지',
            'price' : '가격',
        }