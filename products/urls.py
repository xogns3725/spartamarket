from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.products, name="products"),
    # path("<int:pk>/", views.article_detail, name="article_detail"),
    # path("create/", views.create, name="create"),
    # path("<int:pk>/delete/", views.delete, name="delete"),
    # path("<int:pk>/update/", views.update, name="update"),
    # path('hello/', views.hello, name="hello"),
    # path("data-throw/", views.data_throw, name="throw"),
    # path("data-catch/", views.data_catch, name="catch"),
    # path("index/", views.index, name="index"),
    # path("<int:pk>/comments/", views.comments_create, name="comments_create"),
    # path("<int:pk>/comments/<int:comment_pk>/delete/", views.comment_delete, name="comment_delete"),
    # path("<int:pk>/like/", views.like, name="like"),
]
