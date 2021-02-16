from django.contrib import admin
from django.urls import path
from karmaapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('cart/',views.cart,name='cart'),
    path('category/',views.category,name='category'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('login/',views.login,name='login'),
    path('singleblog/',views.singleblog,name='singleblog'),
    path('singleproduct/',views.singleproduct,name='singleproduct'),
    path('tracking/',views.tracking,name='tracking'),
]
