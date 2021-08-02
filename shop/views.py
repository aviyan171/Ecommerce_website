from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.
def index(request):
    # print(all_products)
    # n=len(all_products)
    # nslides=n//4 +ceil((n/4)-(n//4))
    
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    parameter={'allProds':allProds }
    return render(request,"shop/index.html", parameter)

    # allprods=[[all_products,range(1,nslides),nslides],
    #         [all_products,range(1,nslides),nslides]]

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are  at contact")

def tracker(request):
    return HttpResponse("We are  at tracker")

def Search(request):
    return HttpResponse("We are  at Search")

def Productview(request):
    return HttpResponse("We are  at Productview")

def Checkout(request):
    return HttpResponse("We are  at check out")