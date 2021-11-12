from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book,Order
from django.contrib import messages
from customer.filters import BookFilter
from .decorators import login_required
def signup(request):
    form=forms.UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"customer/signup.html",{"form":form})
    return render(request,"customer/signup.html",context)

def signin(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user=authenticate(request,username=user_name,password=password)
            if user:
                login(request,user)
                return redirect("userhome")
            else:
                messages.error(request,"invalid user")
                return redirect("signin")
    return render(request,"customer/login.html",context)

@login_required
def signout(request,*args,**kwargs):

    logout(request)
    return redirect("signin")


@login_required
def user_home(request,*args,**kwargs):

    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"customer/user.html",context)


@login_required
def order_create(request,p_id,*args,**kwargs):

    book=Book.objects.get(id=p_id)
    form=forms.OrderForm(initial={"product":book})
    context={"form":form,"book":book}
    if request.method=="POST":
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()
            messages.success(request,"order placed")
            return redirect("myorders")
        else:
            return render(request, "customer/order_create.html", {"form":form})

    return render(request,"customer/order_create.html",context)


@login_required
def myorders(request,*args,**kwargs):

    orders=Order.objects.filter(user=request.user).exclude(status="cancelled")
    context={"orders":orders}
    return render(request,"customer/myorders.html",context)


@login_required
def cancel_order(request,id,*args,**kwargs):
    orders=Order.objects.get(id=id)
    # print("id",id)
    orders.status="cancelled"
    orders.save()
    return redirect("myorders")


# djangofilter

@login_required
def booksearch(request,*args,**kwargs):
    filters=BookFilter(request.GET,queryset=Book.objects.all())
    return render(request,"customer/booksearch.html",{"filter":filters})

