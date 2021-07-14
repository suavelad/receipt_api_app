from django.db import models

# Create your models here.


class Receipts(models.Model):
    customer_name = models.TextField()
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField(null=True,blank=True)
    cashier_user = models.IntegerField()
    ref= models.CharField(max_length=20,null=True,blank=True)
    item = models.CharField(max_length=250)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        self.ref



class Receipt_ref(models.Model):
    cashier_user = models.IntegerField()
    ref= models.CharField(max_length=250)
    quantity = models.IntegerField()
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        self.ref