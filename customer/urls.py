from django.urls import path
from customer import views

urlpatterns=[
    path('accounts/signup',views.signup,name="signup"),
    path('accounts/signin',views.signin,name="signin"),
    path('accounts/signout',views.signout,name="signout"),
    path('userhome',views.user_home,name="userhome"),
    path('orders/add/<int:p_id>',views.order_create,name="ordercreate"),
    path('orders',views.myorders,name="myorders"),
    path('order/remove/<int:id>',views.cancel_order,name="cancelorder"),
    path('books/find',views.booksearch,name="booksearch"),

]