import django_filters
from .models import *
from django_filters import DateFilter;
class OrderFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="created_at",lookup_expr="gte")#greater than or equl(gte)
    end_date=DateFilter(field_name="created_at",lookup_expr="lte")#lessthan or equal(lte)
    class Meta:
        model=Order
        fields="__all__"
        exclude=['customer','created_at']

