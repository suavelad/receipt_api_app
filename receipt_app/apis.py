from .serializers import UserSerializer
from .schemas import ReceiptSchema
from .models import Receipts
from django.db import connection
import collections
from rest_framework import  permissions,generics
from django.core.exceptions import ValidationError
from rest_framework_bulk import  ListBulkCreateUpdateDestroyAPIView


class ReceiptView(ListBulkCreateUpdateDestroyAPIView):

    schema =ReceiptSchema
    queryset = Receipts.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    


 


