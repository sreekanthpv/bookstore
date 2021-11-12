import django_filters
from owner.models import Book
from django import forms

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=["book_name","author","price"]

        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"})
        }