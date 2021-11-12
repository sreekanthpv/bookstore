from django.shortcuts import render,redirect
from owner import forms
from owner.models import Book,Order
from django.db.models import Count
from customer.filters import BookFilter
from django.contrib.auth import logout

def registration(request):
    form=forms.Registration()
    context={}
    context['form']=form
    if request.method=="POST":
        form=forms.Registration(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            print(firstname,lastname,email,password)
            return redirect("login")
        else:
            return render(request,"registration.html",{"form":form})

    return render(request,'registration.html',context)

def login(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
       form=forms.LoginForm(request.POST)
       if form.is_valid():
           username=form.cleaned_data['username']
           password=form.cleaned_data['password']
           print(username,password)
           return redirect("booklist")
       else:
           return render(request,"login.html",{"form":form})
    return render(request,"login.html",context)

def signout(request):
    logout(request)
    return redirect("login")




def addbook(request):
    form=forms.AddBookForm()
    context={}
    context['form']=form
    if request.method == "POST":
        form=forms.AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            # bookname=form.cleaned_data['bookname']
            # author=form.cleaned_data['author']
            # price=form.cleaned_data['price']
            # copies=form.cleaned_data["copies"]
            # print(bookname,author,price,copies)
            # book=Book(book_name=bookname,author=author,price=price,copies=copies)
            # book.save()
            return redirect("booklist")
        else:
            return render(request, 'addbook.html', {"form":form})


    return render(request,'addbook.html',context)



def booklist(request):
    form=forms.BookSearchForm()
    books=Book.objects.all()
    context={}
    context["books"]=books
    context["form"]=form
    if request.method=="POST":
        form=forms.BookSearchForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data["book_name"]
            books=Book.objects.filter(book_name__contains=book_name)
            print(books)
            context["books"]=books
            return render(request,"booklist.html",context)


    return render(request,"booklist.html",context)

def bookdetail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"bookdetails.html",context)


def book_update(request,id):
    book=Book.objects.get(id=id)

    # data={
    #     "bookname":book.book_name,
    #     "author":book.author,
    #     "price":book.price,
    #     "copies":book.copies,
    #
    # }
    form=forms.BookChangeForm(instance=book)  #(initial=data) is changed to (instance=book) means created an instance of book object
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.BookChangeForm(request.POST,instance=book,files=request.POST)
        if form.is_valid():
            # b_name=form.cleaned_data["bookname"]
            # author=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # copies=form.cleaned_data["copies"]
            #
            # book.book_name=b_name
            # book.author=author
            # book.price=price
            # book.copies=copies
            form.save()
            return redirect("booklist")
    return render(request,"book_update.html",context)

def book_remove(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("booklist")

def dashboard(request):
    reports=Order.objects.values("product__book_name").annotate(counts=Count("product"))
    orders=Order.objects.filter(status="ordered")
    stocks=Book.objects.all().order_by("copies")
    context={"orders":orders,"reports":reports,"stocks":stocks}
    return render(request,"dashboard.html",context)

def orderedit(request,id):
    order=Order.objects.get(id=id)
    form=forms.OrderEditForm(instance=order)
    context={"order":order,"form":form}
    if request.method=="POST":
        form=forms.OrderEditForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request,"orderedit.html",context)

def ownerbase(request):
    return render(request,"base.html")





