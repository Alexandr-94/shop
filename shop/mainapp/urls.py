from .views import test_view, ProductDetailViews
from django.urls import path

urlpatterns = [
    path('', test_view, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailViews.as_view(), name='product_detail')
]


