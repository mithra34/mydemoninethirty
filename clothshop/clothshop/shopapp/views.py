from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from shopapp.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
import sys
def  home(request,c_slug=None):
    c_page=None
    products_list=None

    products=Product.objects.filter(stock=10)

    return render(request, 'home.html', {'products': products})











def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:

        products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)

    try:
        page=int(request.GET.get('page','1'))

    except:
        page = 1


    try:

        products=paginator.page(page)
    except (EmptyPage,InvalidPage):

        products=paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})



def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e :
        raise e
    return  render(request,'product.html',{'product':product})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')