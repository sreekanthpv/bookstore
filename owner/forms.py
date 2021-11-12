from django import forms
from owner.models import Book,Order
from django.forms import ModelForm


class Registration(forms.Form):

    firstname=forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    lastname=forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        firstname=cleaned_data["firstname"]
        a="1234567890"
        for i in a:
         if i in firstname:
            msg="invalid firstname"
            self.add_error("firstname",msg)
            break

        lastname=cleaned_data["lastname"]
        for i in a:
            if i in lastname:
                msg="invalid lastname"
                self.add_error("lastname",msg)
                break





class LoginForm(forms.Form):

    username = forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data["username"]
        sym="!@#$%^&*())"
        for i in sym:
            if i in username:
                msg="symbols are not accepted"
                self.add_error("username",msg)
                break


class AddBookForm(ModelForm):
    class Meta:# for adding additional information
        model=Book
        fields="__all__"
        widgets={
           "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "copies":forms.TextInput(attrs={"class":"form-control"}),
        }

        labels={
            "book_name":"books names",
            "author":"authors",
        }


    # bookname = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        book_name=cleaned_data["book_name"]
        books=Book.objects.filter(book_name=book_name)
        if books:
            msg="repeated book"
            self.add_error("book_name",msg)


        price=cleaned_data["price"]
        if int(price) < 0:
            msg="invalid price"
            self.add_error("price",msg)

        copies=cleaned_data["copies"]
        if int(copies) < 0:
            msg="invalid copies"
            self.add_error("copies",msg)

class BookChangeForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        # bookname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
        # author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
        # price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
        # copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))


class BookSearchForm(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))


class OrderEditForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["status","expected_delivery_date"]

        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_delivery_date":forms.DateInput(attrs={"type":"date"}),

        }

