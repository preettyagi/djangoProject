from django.db import models

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=250)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT)
    promotions = models.ManyToManyField('Promotion')



class Customer(models.Model):

    MEMBERSHIP_CATAGORIES = [
        ['S', 'Silver'],
        ['B', 'Bronze'],
        ['G', 'Gold']
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CATAGORIES)



class Order(models.Model):
    ORDER_STATUS = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=ORDER_STATUS, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



class Addresss(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)



class orderItem(models.Model):
    #name = models.CharField(max_length=250)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)    



class cartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()



class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()
