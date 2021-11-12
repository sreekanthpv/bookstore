from django.urls import path
from owner import views

urlpatterns = [
    path('accounts/signup', views.registration, name='signup'),
    path('accounts/signin', views.login, name='login'),
    path('accounts/signout',views.signout,name="ownersignout"),
    path('books/add',views.addbook,name='addbook'),
    path('books',views.booklist,name="booklist"),
    path('books/details/<int:id>',views.bookdetail,name='bookdetail'),
    path('books/change/<int:id>',views.book_update,name="bookupdate"),
    path('books/delete/<int:id>',views.book_remove,name="bookremove"),
    path('',views.dashboard,name="dashboard"),
    path('books/order/edit/<int:id>',views.orderedit,name="orderedit"),
    path("base",views.ownerbase,name='ownerbase'),

]
