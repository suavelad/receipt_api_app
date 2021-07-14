from django.db.models.fields import FloatField
from rest_framework import serializers
from .models import Receipts
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from rest_framework_bulk import   BulkListSerializer,BulkSerializerMixin
  


class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

class ReceiptSerializer(serializers.ModelSerializer):

     class Meta:
        model = Receipts
        fields = '__all__'   
        # read_only =('id','total','cashier_user')  
        # # list_serializer_class = BulkCreateListSerializer  
   

class ReceiptsSerializer(serializers.ModelSerializer):
    customer_name= serializers.CharField(required=True)
    customer_phone=serializers.CharField(required=True)
    customer_address = serializers.CharField(required=True)
    item = serializers.CharField(required=True)
    unit_price = serializers.FloatField(required=True)
    quantity = serializers.FloatField(required=True)
    description =serializers.CharField(required=False) 
    cashier_user = serializers.IntegerField(required=False)
    id = serializers.IntegerField(required=False)
    total =serializers.FloatField(required=False)

    class Meta:
        model = Receipts
        fields = '__all__'   
        read_only =('id')  
        list_serializer_class = BulkCreateListSerializer  


    def create(self,  validated_data):
        requestx=self.context['request']
        cashier_userx= requestx.user.id
        customer_name=validated_data['customer_name']
        customer_phone=validated_data['customer_phone']
        customer_address = validated_data['customer_address'] 
        item = validated_data['item'] 
        unit_price = validated_data['unit_price']
        quantity = validated_data['quantity'] 
        total = unit_price * quantity

        the_data = Receipts.objects.create( **validated_data,total=total, cashier_user=cashier_userx)
        # the_data = Receipts.objects.bulk_create( **validated_data,total=total, cashier_user=cashier_userx)

        # the_data = Receipts( **validated_data,total=total, cashier_user=cashier_userx)

        the_data.save()


        return the_data


class UserListSerializer(serializers.ListSerializer):

    def validate (self, validated_data):
         if len(validated_data) >= 10 :
             return validated_data

         else:
            raise serializers.ValidationError({ 
                'message': 'You are about creating less than 10 receipts '
            })
#
    def create(self, validated_data):

        # try:     

        if len(validated_data) >= 10 :
            requestx=self.context['request']
            cashier_userx= requestx.user.id

            the_data = [Receipts(**item,total=item['unit_price'] * item['quantity'],cashier_user=cashier_userx) for item in validated_data]
            return Receipts.objects.bulk_create(the_data)
        else:
            the_data= []
            return Receipts.objects.bulk_create(the_data)


   
class UserSerializer(serializers.Serializer):
    customer_name= serializers.CharField(required=True)
    customer_phone=serializers.CharField(required=True)
    customer_address = serializers.CharField(required=True)
    item = serializers.CharField(required=True)
    unit_price = serializers.FloatField(required=True)
    quantity = serializers.FloatField(required=True)
    description =serializers.CharField(required=False) 
    cashier_user = serializers.IntegerField(required=False)
    id = serializers.IntegerField(required=False)
    total =serializers.FloatField(required=False)

       
    class Meta:
        list_serializer_class = UserListSerializer
