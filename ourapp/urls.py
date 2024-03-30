
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Home,name="home-page"),

    path('shop/',views.shop,name="shop-page"),

    path('about/',views.aboutus,name="about-page"),

    path('contact/',views.contact,name="contact-page"),
 
    path('detail/',views.detailpage,name="detail-page"),

    path('cart/',views.cartpage,name="cart-page"),

    path('checkout/',views.checkout,name="checkout-page"),

    path('order_success/',views.thankpage,name="thankyou-page"),

]
