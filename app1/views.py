from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Customer
from store.models import Product

# Create your views here.

def say_hello(request):
    """
    query_set = Customer.objects.all() #when return a query_set
    query_set.filter().filter().order_by()
    customer = Customer.objects.get(pk=1)

    #Product: inventory<10 and price < 20
    query_set = Product.objects.filter(inventory__lt = 10, price_lt = 20)
    #Product: inventory<10 or price < 20
    query_set = Product.objects.filter(Q(inventory__lt = 10) | Q(price_lt = 20))

    product_title = Product.objects.filter(orderitem__product_id = )
    """
    customer = Customer.objects.raw('select * from store_customer limit 3')

    #return HttpResponse("Hello world! This is django proj")
    return render(request, 'hello.html', {'name': customer[0].first_name})


