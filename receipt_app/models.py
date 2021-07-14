from django.db import models
from auth_api.models import User

# Create your models here.


class Receipts(models.Model):
    customer_name = models.TextField()
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField(null=True,blank=True)
    cashier_user = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='cashier_user')
    item = models.CharField(max_length=250)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        self.ref


