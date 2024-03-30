from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')


def aboutus(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def detailpage(request):
    return render(request,'shopsingle.html')

def cartpage(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def thankpage(request):
    return render(request,'thankyou.html')



