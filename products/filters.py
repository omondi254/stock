import django_filters
from products .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['item_name']

class CategoryFilter(django_filters.FilterSet):
    class Meta: 
        model = Category
        fields = ['name']