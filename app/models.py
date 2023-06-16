from django.db import models

# Create your models here.
class Customer(models.Model):
    Cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    id=models.IntegerField(primary_key=True)
    date=models.DateField()
    order_item=models.CharField(max_length=100)
    Cid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.order_item
