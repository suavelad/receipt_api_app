from django.db.models.fields import FloatField
from rest_framework import serializers
from .models import Receipts
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class UserListSerializer(serializers.ListSerializer):


    @property
    def custom_full_errors(self):
        """
        Returns full errors formatted as per requirements
        """
        default_errors = self.errors
        field_names = []
        for field_name, field_errors in default_errors.items():
            field_names.append(field_name)
        return {
            'code':140,
            'message': 'You are about creating less than 10 receipts',
            'resolve': 'Kindly update your application'
            }

    def validate (self, validated_data):
         if len(validated_data) >= 10 :
             return validated_data

         else:
             raise custom_full_errors()
            # raise serializers.ValidationError({ 
            #     'code': 140,
            #     'message': 'You are about creating less than 10 receipts',
            #     'resolve': 'Kindly update your application'
            # })
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
