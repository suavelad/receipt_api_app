from rest_framework import serializers
from .models import Receipts




class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, args, *kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)



class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = '__all__'       

