from django import forms
from . models import Book


# name,author,bookdesc,bookprice
class Edit_Blog(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','author','bookdesc','bookprice')

class Purchase_book(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','bookprice')